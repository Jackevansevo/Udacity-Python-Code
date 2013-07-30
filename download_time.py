# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

import time

def download_time(filesize, memtype, bandwidth, bandtype):

	# Convert the file sizes to bits s

	if memtype == "kb":
		file_bits = (filesize*(2**10))

	elif memtype == "kB":
		file_bits = (filesize*(2**10)*8)

	elif memtype == "Mb":
		file_bits = (filesize*(2**20))
	elif memtype == "MB":
		file_bits = (filesize*(2**20)*8)

	elif memtype == "Gb":
		file_bits = (filesize*(2**30))

	elif memtype == "GB":
		file_bits = (filesize*(2**30)*8)

	elif memtype == "Tb":
		file_bits = (filesize*(2**40))

	elif memtype == "TB":
		file_bits = (filesize*(2**40)*8)

	else:
		return ("Invalid unit of filesize")


	# Conver the bandwidth into bits

	if bandtype == "kb":
		band_bits = (bandwidth*(2**10))

	elif bandtype == "kB":
		band_bits = (bandwidth*(2**10)*8)

	elif bandtype == "Mb":
		band_bits = (bandwidth*(2**20))

	elif bandtype == "MB":
		band_bits = (bandwidth*(2**20)*8)

	elif bandtype == "Gb":
		band_bits = (bandwidth*(2**30))

	elif bandtype == "GB":
		band_bits = (bandwidth*(2**30)*8)

	elif bandtype == "Tb":
		band_bits = (bandwidth*(2**40))

	elif bandtype == "TB":
		band_bits = (bandwidth*(2**40)*8)

	else:
		return ("Invalid unit of filesize")


	# Now calculate how long it takes to download
	download_secs = float(file_bits / band_bits)
	time_breakdown = time.strftime('%H hours, %M minutes, %S seconds', time.gmtime(download_secs))

	print ("\n\nFile size: %d bits \nBits uploaded per second: %d \nSeconds taken: %f\n") \
	% (file_bits, band_bits, download_secs) + ">>> " + time_breakdown



download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

