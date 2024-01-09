#password generator
import secrets
import array
import random

lowercase= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z']


numbers= ['1', '2', '3', '4', '5', '6', '7', '8', '9','0']


uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z']


special_chars = ['@', '#', '$', '%', '=', ':', '?','/', '|', '~', '>',  
           '*', '(', ')', '<']


combined_list= lowercase+uppercase+numbers+special_chars

pswd_len= int(input("Enter the length of the password:"))

genpass = ''

for i in range(pswd_len):
    genpass+= ''.join(secrets.choice(combined_list))

print(f"The generated password for specified length is: {genpass}")




