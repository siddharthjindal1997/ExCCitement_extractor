from PyQt4.QtGui import *
from PyQt4.QtCore import *
from gui import Ui_MainWindow
import moviepy.editor
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
from tqdm import *
import os


class excitement_extract():
    """ Where the magic happens! 
    Three processes run in parallel in this class:
    1. detection of scene cuts to finally analyse
        density of cuts.
    2. detection of change in average motion in consecutive 
        frames to analyse movement.
    3. detection of change in sound volume to analyse 
        the excitement in crowd/commentators voice.

    The method for cuts detection is inspired from cut detection 
    tool in moviepy library. Sound analyses part isinspired 
    from the blogpost : 
    Automatic Soccer Highlights Compilations With Python
    which can be found here http://zulko.github.io/

    Parameters
    ----------

    filename
        String that holds the path/to/the/file passed 
        by the GUI

    Attributes
    ----------

    luminosities
        Stores luminosity values of frame image ,
        used for detecting cuts density. 

    threshold
        int value which determines how much change in 
        luminosity has to be considered a cut.

    progress_bar
        boolean value which decides if progress
        bar is to be shown (True or 1) or not (False or 0)

    fps
        number of frames per second to be processed. important 
        to be mentioned specifically since high fps slows down 
        the process

    avg_motion_list
        this list stores the average motion for consecutive frames.
        its scaled between 0 to 100 afterwards by a scaling function.

    cut_density_list
        this list stores the density of cuts at a particular frame 
        location. its scaled between 0 to 100 afterwards by a 
        scaling function.

    sound_list
        this list stores the rms value of sound, thus volume.
        its also scaled afterwards by a scaling function.

    excite_curve
        list has the data for the excitement trend of the match.

    """
    def __init__(self, filename):
        # reading a sports video at a low resolution
        self.clip = moviepy.editor.VideoFileClip(filename,
                                                 target_resolution=(100, None))
        self.luminosities = list()
        self.threshold = 10.0
        self.progress_bar = False
        self.fps = 10.0
        self.avg_motion_list = list()
        self.cut_density_list = list()
        self.sound_list = list()
        self.excite_curve = list()
        print 'file read :' + filename

    def next_cut(self, f_time, cuts_frame_time):
        """ For a frame, it gets the time (in secs) 
        of the next cut in the list.
        """
        for j in cuts_frame_time:
            if(j-f_time > 0):
                break
        return j

    def prev_cut(self, f_time, cuts_frame_time):
        """ For a frame, it gets the time (in secs) 
        of the previous cut in the list.
        """
        for k in reversed(cuts_frame_time):
            if(k-f_time < 0):
                break
        return k

    def process_frames(self):
        """ Process frames and runs algorithms on 
        them to analyse- movement, cuts and sound.
        """
        last_fr = None
        for f in self.clip.iter_frames(fps=self.fps,
                        dtype='uint32', progress_bar=False):
            
            self.luminosities.append(f.sum())
            
            # Analysing average movement
            if last_fr is not None:
                fr_diff = f-last_fr
                self.avg_motion_list += [fr_diff.sum()]
                del(fr_diff)
                del last_fr
            last_fr = f.copy()

        # Detecting cuts in the video
        self.luminosities = np.array(self.luminosities, dtype=float)

        if self.clip is not None:
            end = self.clip.duration
        else:
            end = len(self.luminosities)*(1.0/self.fps)
        lum_diffs = abs(np.diff(self.luminosities))
        avg = lum_diffs.mean()
        luminosity_jumps = 1+np.array(np.nonzero(lum_diffs >
                                                 self.threshold*avg))[0]
        cuts_list = [0] + list((1.0/self.fps) * luminosity_jumps) + [end]

        # Calculating density of cuts
        for i in range(1, int(math.ceil(self.clip.duration*self.fps))):
            self.cut_density_list.append(math.exp((1 -
                                         (excitement_extract.next_cut(self, i /
                                          self.fps, cuts_list) -
                                          excitement_extract.prev_cut(self, i /
                                          self.fps, cuts_list))) / 100))

        # Analysing crowd/commentators sound
        cut = lambda i: self.clip.audio.subclip(1.0 * i / self.fps, 1.0 * (i +
                1) / self.fps).to_soundarray(fps=22000)
        volume = lambda array: np.sqrt(((1.0*array)**2).mean())

        self.sound_list = [volume(cut(i)) for i in
                           range(0, int(self.fps*(self.clip.duration)))]

        self.cut_density_list = excitement_extract.scale_curve(self,
                                        np.asarray(self.cut_density_list))
        self.avg_motion_list = excitement_extract.scale_curve(self,
                                        np.asarray(self.avg_motion_list))
        self.sound_list = excitement_extract.scale_curve(self,
                                        np.asarray(self.sound_list))

        print 'Video processed!'

    def scale_curve(self, unscaled_arr):
        # Scaling the values of array between 0 to 100
        len(unscaled_arr)
        max_val = max(unscaled_arr)
        return unscaled_arr*100/max_val

    def process_highlights(self):
        """ Forms the final curve used for highlights extraction.
        
        Multiplication here is used as logical AND operation. 
        Multiplying curves together amplifies the peaks and the lows.
        We generate two curves in this method.
        kaiser_function(length, alpha) is convoluted with a rough curve 
        to smoothen it out. Longer the smoothing function, and bigger the
        alpha, more smoothing achieved.

        Attributes
        ----------

        multiply_orig_curves
            The original curves are multiplied together and stored
            in a list.

        kaiser_small_window
            Less smoothing required to capture peaks of excitement
            without losing any data.
        
        final_high_times
            list that stores and returns the final position of 
            peaks of excitement


        """
        multiply_orig_curves = [self.cut_density_list[k] *
                self.avg_motion_list[k]*self.sound_list[k]
                for k in range(0, len(self.cut_density_list))]
        
        kaiser_small_window = np.kaiser(len(self.cut_density_list)/50, 10)
        
        multiply_orig_smooth = np.convolve(kaiser_small_window /
                kaiser_small_window.sum(), multiply_orig_curves, mode='same')
        
        self.final_high_times = excitement_extract.get_final_highlights_time(
                self, multiply_orig_smooth)
        
        return self.final_high_times

    def get_excite_curve(self):
        """ Create smooth graph to capture exitement trend
        of the match.

        Attributes
        ----------
        
        kaiser_long_window
            long smoothing function to smoothen curves

        cuts_scaled_smooth, motion_scaled_smooth, sound_scaled_smooth
            the original curves are first smoothen out and then
            multiplied to get the excitement trend of the match stored
            in excite_curve.

        """
        kaiser_long_window = np.kaiser(len(self.cut_density_list)/10, 5)
        
        cuts_scaled_smooth = np.convolve(kaiser_long_window /
                kaiser_long_window.sum(), self.cut_density_list, mode='same')
        
        motion_scaled_smooth = np.convolve(kaiser_long_window /
                kaiser_long_window.sum(), self.avg_motion_list, mode='same')
        
        sound_scaled_smooth = np.convolve(kaiser_long_window /
                kaiser_long_window.sum(), self.sound_list, mode='same')
        
        self.excite_curve = [cuts_scaled_smooth[k] *
                motion_scaled_smooth[k] * sound_scaled_smooth[k]
                for k in range(0, len(self.cut_density_list))]
        
        return self.excite_curve

    def get_final_highlights_time(self, smooth_curve):
        """ Works to detect peaks in the curve obtaied.
        Multiplication (for logical AND) of both increases and
        decreases marks existance of a peak.

        Returns
        -------
        final_peaks_position
            time stamps (in secs) of the final highlights.
        """
        increases = np.diff(smooth_curve)[:-1] >= 0
        decreases = np.diff(smooth_curve)[1:] <= 0
        peaks_position = ((increases * decreases).nonzero()[0])
        peaks_value = smooth_curve[peaks_position]
        peaks_position = peaks_position[peaks_value >
                np.percentile(peaks_value, 90)]

        # filter two close (100 frames apart) peaks
        final_peaks_position = [peaks_position[0]]
        for fr_num in peaks_position:
            if (fr_num - final_peaks_position[-1]) < 100:
                if (smooth_curve[fr_num] > smooth_curve[final_peaks_position[-1]]):
                    final_peaks_position[-1] = fr_num
            else:
                final_peaks_position.append(fr_num)
        return final_peaks_position
