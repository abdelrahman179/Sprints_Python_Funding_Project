""" 
    Name : AbdElrahman Ibrahim Zaki
    Email : abdelrahmanzaki.aez@gmail.com  
    Project : Crowd Funding Console App - login file
"""

from users import users

def logInSys():
    login_email = str(input('Please enter your email: '))
    # validate whether the user is already exist or not
    while login_email not in users:
        print('Invalid Email')
        login_email = str(input('Please re-enter your email: '))

    login_pass = str(input('Hello '+users[login_email]['First_Name']+'. Please enter your password: '))
    # confirm the password
    while login_pass != users[login_email]['Password']:
        print('Incorrect Password')
        login_pass = str(input('Please re-enter your password: '))

    print("\n\n*********** Welcome "+users[login_email]['First_Name']+", you've logged in successfully ***********\n\n")

    # Preview the user projects 
    from projects import userProjects
    userProjects(login_email)

    