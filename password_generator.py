import random
import string

def generate_password(min_length,  numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits 
    special = string.punctuation

    charchters = letters
    if numbers:
        charchters += digits
    if special_chars:
        charchters += special
    pwd=""

    meets_criteria = False
    has_number = False
    has_special = False
    
    while not meets_criteria or len(pwd) < min_length:
      new_char = random.choice(charchters)
      pwd += new_char
      if new_char in digits:
          has_number = True
      elif new_char in special:
          has_special = True
          meets_criteria = True
      if numbers:
          meets_criteria = has_number 
      if special_chars:
          meets_criteria = meets_criteria and has_special
          
    return pwd
min_length = int(input("Enter the minimum length : "))
has_numbers = input("Do you want to hane numbers? (y/n): ").lower() == 'y'
has_special= input("Do you want to have special characters? (y/n): ").lower() == 'y'
pwd= generate_password(min_length, has_numbers, has_special)
print("The generate_password is:",pwd)
