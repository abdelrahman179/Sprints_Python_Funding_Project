""" 
    Name : AbdElrahman Ibrahim Zaki
    Email : abdelrahmanzaki.aez@gmail.com  
    Project : Crowd Funding Console App - validation file
"""

import re
import phonenumbers

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 

# for validating an Email
def email_checker(email):
    # pass the regular expression
    # and the string in search() method
    if(re.match(regex, email)):
        return True
    else:
        return False
 

# for validating a Mobile number
def mobile_checker(mobile):
    # Parsing String to Phone number
    phone_number = phonenumbers.parse(mobile)
    # Validating a phone number
    result = phonenumbers.is_valid_number(phone_number)
    # Checking possibility of a number
    possible = phonenumbers.is_possible_number(phone_number)

    return result
