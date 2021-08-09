""" 
    Name : AbdElrahman Ibrahim Zaki
    Email : abdelrahmanzaki.aez@gmail.com  
    Project : Crowd Funding Console App - projects sub-file
"""
from datetime import datetime
import pandas as pd


projects = [
    {
        'Owner':'abdelrahman@gmail.com',
        'Title': 'project_x',
        'Details': 'This is a test',
        'Total-Target': '25000',
        'Start-Date': '2021-11-01',
        'End-Date': '2021-12-31'
    },
    {
        'Owner': 'omar@gmail.com',
        'Title': 'project_y',
        'Details': 'This is a test',
        'Total-Target': '25000',
        'Start-Date': '2021-11-01',
        'End-Date': '2021-12-31'
    },
    {
        'Owner': 'omar@gmail.com',
        'Title': 'project_z',
        'Details': 'This is a test',
        'Total-Target': '25000',
        'Start-Date': '2021-11-01',
        'End-Date': '2021-12-31'
    },
    {
        'Owner': 'omar@gmail.com',
        'Title': 'project_v',
        'Details': 'This is a test',
        'Total-Target': '25000',
        'Start-Date': '2021-11-01',
        'End-Date': '2021-12-31'
    },
    {
        'Owner': 'khaled@gmail.com',
        'Title': 'Khaled_p1',
        'Details': 'This is a test',
        'Total-Target': '25000',
        'Start-Date': '2021-11-01',
        'End-Date': '2021-12-31'
    }
]


def allProjects():
    if (not projects):
        print("There are no projects to preview yet !!\n")
    else:
        ''' Print out all projects using pandas  '''
        project = pd.DataFrame(projects)
        print(project)



def userProjects(user_email):
    for index in range(len(projects)):
        for val in projects[index]:
            if user_email in projects[index][val]: 
                print(projects[index].items())



