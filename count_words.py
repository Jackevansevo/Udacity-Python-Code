# Write a procedure, count_words, which takes as input a string
# and returns the number of words in the string. You may consider words
# as strings of characters separated by spaces.



def count_words(passage):
	# Reject empty list
	if passage == (""):
			return 0
	# instead of counting the number of words count the number of whitespace
	whitespaces = 0
	for c in passage:
		# add to the count of spaces
		if c == " ":
			whitespaces += 1
		
	return whitespaces + 1
	# Add 1 onto the number of whitespaces for the trailing whitespace at end of passage





passage =("The number of orderings of the 52 cards in a deck of cards " # 13
"is so great that if every one of the almost 7 billion people alive " # 
"today dealt one ordering of the cards per second, it would take " # 
"2.5 * 10**40 times the age of the universe to order the cards in every " # 
"possible way.") # 2
print count_words(passage)
#>>>56

quote = ("")
print count_words(quote)