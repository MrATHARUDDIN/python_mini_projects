import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
#This line builds a string of all possible characters you might want to use in encoding or encryption.

# Converting to a List (type casting)
chars = list(chars)
key = chars.copy() # Make a copy

print(f"chars : {chars}")
print(f"Keys : {key}")