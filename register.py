""" 
    Name : AbdElrahman Ibrahim Zaki
    Email : abdelrahmanzaki.aez@gmail.com  
    Project : Crowd Funding Console App - login file
"""
from users import users

def registeration():
    reg_1st_name = str(input('Please enter your first name: '))
    reg_last_name = str(input('Please enter your last name: '))
    reg_email = str(input('Please enter your email: '))

    # validate the entered email
    from validation import email_checker
    email_check = email_checker(reg_email)
    while email_check == False:
        reg_email = str(input('Please enter a valid email: '))
        email_check = email_checker(reg_email)

    # if the email already exists
    while reg_email in users:
        reg_email = str(input('The email is already used by another user, retry using other email: '))


    reg_password = str(input('Please enter your Password: '))
    reg_conf_pass = str(input('Please confirm your Password: '))
    while reg_conf_pass != reg_password:
        reg_conf_pass = str(input('Password does not match, re-confirm your password: '))

    reg_mobile = str(input('Please enter your mobile: '))

    # validate the entered mobile
    from validation import mobile_checker
    mobile_check = mobile_checker(reg_mobile)
    while reg_mobile == False:
        reg_mobile = str(input('Please enter a valid mobile number: '))
        mobile_check = mobile_checker(reg_mobile)

    # Store the new user data
    users.update({reg_email : 
                  {
                    "First_Name" : reg_1st_name,
                    "Last_Name" : reg_last_name,
                    "Password" : reg_password,
                    "Mobile" : reg_mobile
                  }
                })

    print("\n\n*********** You've already registered successfully ***********\n\n")

    #verify whether the user data is stored or not 
    #print(users)