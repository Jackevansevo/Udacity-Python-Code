# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]

def lookup(index,keyword):
	x = 0
	for entry in index:
		if entry[x] == keyword:
			return entry[x+1]
	return ("Entry not found")





print lookup(index,'udacity')
print lookup(index, 'computing')
print lookup(index, 'fobar')
#>>> ['http://udacity.com','http://npr.org']
