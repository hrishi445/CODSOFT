import secrets
import string
import random

letters= string.ascii_letters

numbers= string.digits

special_chars= string.punctuation

combined_list= letters+numbers+special_chars

pswd_len= int(input("Enter the length of the password:"))

genpass = ''
for i in range(pswd_len):
    genpass+= ''.join(secrets.choice(combined_list))

print(f"The generated password for specified length is: {genpass}")
