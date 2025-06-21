import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
#This line builds a string of all possible characters you might want to use in encoding or encryption.

# Converting to a List (type casting)
chars = list(chars)
key = chars.copy() # Make a copy


random.shuffle(key) # it will change the value randomly 
# print(f"chars : {chars}")
# print(f"Keys : {key}")


#Entrypted
text_en = input("Enter a message to encrypt: ")
cipher_text = " "

for letter in text_en:
    index = chars.index(letter)
    cipher_text +=key[index]

print(f"Orginale message {text_en}")
print(f"Encrypted message {cipher_text}")

# Decrypted
cipher_text = input("Enter a message to Decrypted: ")
text_en = " "

for letter in cipher_text:
    index = key.index(letter)
    text_en += chars[index]

print(f"Orginale message {cipher_text}")
print(f"Decrypted message {text_en}")