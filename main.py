""" 
    Name : AbdElrahman Ibrahim Zaki
    Email : abdelrahmanzaki.aez@gmail.com  
    Project : Crowd Funding Console App - main file
"""
import pandas as pd

''' ------- Greeting ------- '''
print(" ---- Welcome to Crowd-Funding ---- ")
print("\n\n \t ------------ \n\n")

""" ------- Preview all projects ------- """
from projects import allProjects
# Call preview projects function
allProjects()


""" ------- Ask the user to login or register ------- """
authentication = str(input("Enter (login) if you have an account \nEnter (register) if you're a new user \n Your input: "))

while(authentication != 'login' and authentication != 'register'):
    print("Invalid input \n")
    authentication = str(input("Enter (login) if you have an account \nEnter (register) if you're a new user \n Your input: "))


''' ------- Login System ------- '''
if authentication == 'login':
    from login import logInSys
    # Call login function 
    logInSys()

''' ------- Registeration ------- '''
if authentication == 'register':
    from register import registeration
    # Call registeration function 
    registeration()
    
    