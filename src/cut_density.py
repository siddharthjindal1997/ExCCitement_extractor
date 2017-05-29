#
#

class cut_detect:
	"""
	detects the density of cuts
	
	Attributes
	----------
	threshold:
		the threshhold value difference between
	block_size:
		number of rows and columns to be iterated in one go.
	Methods
	-------
	calc_average()
		returns the average of pixel value of a frame.
	frame_process()
		actual calculations happen here, compare difference
		between curr_frame average and last_frame_avg to the threshold value.
	post_process()
		creates a list of the cuts detected in form of frame number.
	calc_density()
		calculate the cut density by formula.
"""


def process_frame:
	"""
	Parameters
	----------
	curr_frame: `numpy.ndarray`
		the data array of the input kth frame image
	last_frame_avg:`float`
		average pixel value over the last frame.
	threshold: `float`
		minimum change in average for a cut to be registered
	Returns
	-------
	cuts[]: `list`
		list of frame numbers containing the cut positions
"""
