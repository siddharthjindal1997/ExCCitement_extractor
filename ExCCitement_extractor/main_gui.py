from PyQt4.QtGui import *
from PyQt4.QtCore import *
from gui import Ui_MainWindow
from excitement_algo import excitement_extract
import moviepy.editor
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import os
# import pandas as pd

class MyMainGui(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainGui, self).__init__(parent)
        self.setupUi(self)
        self.filename = None

        #self.activecheck=True

        self.butLoadFile.clicked.connect(self.load_file)
        self.actionLoad.triggered.connect(self.load_file)

        self.butGenGraph.clicked.connect(self.process_manager)

        



        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)

        #sys.stderr = EmittingStream(textWritten=self.normalOutputWritten)

        self.buExit.clicked.connect(self.exit_gui)
        self.actionExit.triggered.connect(self.exit_gui)

    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__

    

    def normalOutputWritten(self, text):
        # Append text to the QTextEdit widget.
        #self.textandstuff.append(text)
        cursor = self.textandstuff.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.textandstuff.setTextCursor(cursor)
        self.textandstuff.ensureCursorVisible()
        #QApplication.processEvents()

    def load_file(self):
        # Load a video file from directory.
        self.filename = QFileDialog.getOpenFileName(self)

    def process_manager(self):
        """Important control function which calls the
        appropriate functions at appropriate times and manages
        the flow of the processes.

        Attributes
        ----------

        game_clip
            main object of excitement_extract class which goes 
            through the processes of highlights extraction. 

        highlight_list
            list of times (in seconds) of the detected peaks 
            of the excitement curve.
        
        excitement_curve
            this list holds the smoothen out curve which shows
            the trends of change in the exitement of the match.

        pixmap
            It is an object of QPixmap class which shows the 
            excitement curve of the match in the GUI window.

        """
        self.isGraphgenerated = True
        game_clip = excitement_extract(str(self.filename))
        self.butCancel.clicked.connect(game_clip.stop_process)
        print "The algorithm is running, please be patient..."
        print "It might take some time."
        check_complete = game_clip.process_frames()
        if check_complete==1:
            print "Process stopped in the middle by user."
            print "====================================="
            return
        highlight_list = game_clip.process_highlights()
        excitement_curve = game_clip.get_excite_curve()
        my_gui.sec_to_hms(highlight_list)
        plt.plot(excitement_curve)
        my_gui.createfolder()
        plt.savefig(str(self.filename) + 'folder/testplot.png')
        pixmap = QPixmap(str(self.filename) + 'folder/testplot.png')
        ScaledPixmap = pixmap.scaled(self.label.size())
        self.label.setPixmap(ScaledPixmap)
        self.label.show()
        print 
        
        final = moviepy.editor.concatenate([game_clip.clip.subclip(max(t-10,0),min(t+5, game_clip.clip.duration))
                     for t in highlight_list])
        final.to_videofile(str(self.filename) + 'folder/summary.mp4')

        print "Extraction completed!"
        print "==================================="


    def createfolder(self):
        """ Creates a new folder for each new file being
        processed and save the extracted highlights and 
        the excitement curve image (as *.jpg)

        """
        if not os.path.exists(str(self.filename)+'folder'):
            print "saving graph in a new folder named : %sfolder" %str(
                self.filename)
            os.makedirs(str(self.filename)+'folder')

    def sec_to_hms(self, highlight_list):
        """Converts the highlights time list from seconds 
        to hour:mimute:seconds format for better readibility
        and prints it.

        Parameters
        ----------

        highlight_list
            list of times (in seconds) of the detected peaks 
            of the excitement curve.


        """
        print "highlights found at time :",
        for seconds in highlight_list:
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            print " %d:%02d:%02d," % (h, m, s),

    def exit_gui(self):
        """ Exit from the GUI """
        app.exit()


class EmittingStream(QObject):
    """To channel the text to QTextEdit widget
    that was being printed in the terminal.

    """
    textWritten = pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        print ' '





if __name__ == "__main__":
    app = QApplication([])
    my_gui = MyMainGui()
    my_gui.show()
    app.exit(app.exec_())
