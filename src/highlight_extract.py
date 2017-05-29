#
#

class exitement_curve:
	"""
	Attributes
	----------
	v1	parameter weight for curve 1
	v2	parameter weight for curve 2
	v3	parameter weight for curve 3
	
	Methods
	-------
	amplify_high()
		main algorithm which decides which maxima are amplified and
		which are neglected
	calc_wavg()
		calculate the weighted average of the three curves obtained to
		get final exitement curve
	highlight_final()
		returns the final time graph of with Highlights as peaks
	"""
