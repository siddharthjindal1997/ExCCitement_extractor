# Thus file contains the sound analysis part for excitement 
# measurement
# 

class sound_exitement:
	"""
	detect total exitement level of sound

	Attributes
	----------
	samples:number of samples per frame
	
	Methods
	-------
	pre_process()
		convert video to sound array, calculate number of samples
		per frame for video
	process_sound()
		do actual calculation of power spectrum.
	post_process()
		generate list of power spectrum values to create the time
		series.
	"""
	
	
def process_sound():
	"""
	Parameters
	----------
	samples:`int`
		number of audio samples per frame.
	audio_clip: `numpy.array`
		the sample audio array.
	
	Returns
	-------
	energy_spectrum:`float`
		power spectrum value for a frame
	"""
