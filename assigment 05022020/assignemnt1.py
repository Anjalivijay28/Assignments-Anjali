'''
selenium assignment :1
login
click on Assign Leave > get the page heading > Go back to Dashboard
click on Leave List > get the page heading > Go back to Dashboard
click on Timesheet > get the page heading > Go back to Dashboard
logout

selenium assignment :2
Login with Invalid Credentials and capture the login failure message

'''

from selenium import webdriver

class website():

    def __init__(self):
        self.driver=webdriver.Chrome(executable_path="//Users/anjalinairandayil//PycharmProjects//Assignments-Anjali//drivers//chromedriver")
