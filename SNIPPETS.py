############# SNIPPETS #############################

# REVERSE_SECOND_SPLIT_BY_INDEX ()
#
# This line of code first splits the string s by - to get the string
# representing the absolute value of the number (s.split('-')[1]). Then
# it reverses that string (reversed(s.split('-')[1])). Finally, it joins
# the reversed list of characters into a string (''.join(reversed(s.split('-')[1]))).
#
# s = s.split('-')[1]
# s = ''.join(reversed(s))
#
# s = ''.join(reversed(s.split('-')[1]))

# The join() method is necessary in the context of the original code in order to
# produce the final reversed string. Here's why:

# The reversed() function in Python doesn't return a string, but rather an iterable
# object that yields the characters in reverse order. We can't directly convert this
# into a string, so the join() method is used to concatenate all of the characters
# together into a single string.
# However, if you want to reverse a string in Python, you can actually use slicing quite
# easily and efficiently without having to use reversed() or join(). The code can be made
# simpler as follows:
#
# REVERSE_SECOND_PORTION
# s = s.split('-')[1][::-1]
