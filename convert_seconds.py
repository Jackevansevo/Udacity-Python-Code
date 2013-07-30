# Write a procedure, connly anymorevert_seconds, which takes as input a non-negative 
# number of seconds and returns a string of the form 
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes, 
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3

import datetime

def convert_seconds(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    
    if h == 1 or h == 0:
        return "%d hour, %d minutes, %d seconds" % (h, m, s)
    
    else:
        return "%d hours, %d minutes, %d seconds" % (h, m, s)


    

print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds