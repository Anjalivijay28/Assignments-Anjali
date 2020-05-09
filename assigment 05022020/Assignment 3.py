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
import time

class website():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="//Users//anjalinairandayil//PycharmProjects//Assignments-Anjali//drivers//chromedriver")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def login(self,username,password):
        print("Login Started")
        self.driver.find_element_by_name("txtUsername").send_keys(username)
        self.driver.find_element_by_name("txtPassword").send_keys(password)
        self.driver.find_element_by_name("Submit").click()
        time.sleep(5)
        try:
            if self.driver.find_element_by_id("welcome").is_displayed():
                print("Logged in successfully")
        except:
            print(self.driver.find_element_by_id("spanMessage").text)
            return 1
        print("Login Completed")

    def quickresponse(self,quicktest):
        self.driver.find_element_by_xpath("//span[text()='" + quicktest + "']").click()
        time.sleep(3)
        pageHeading = self.driver.find_element_by_xpath("//div[@class='head']/h1").text
        self.driver.find_element_by_id("menu_dashboard_index").click()
        # print(pageHeading)
        return pageHeading


    def logout(self):
        print ("Logout Started")
        self.driver.find_element_by_id("welcome").click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li[2]/a').click()
        try :
            if self.driver.find_element_by_id("logInPanelHeading").is_displayed():
                print ("User logged out successfully")
        except:
            print("Try Again")

web_1 = website()
unm = input("Enter user Name : ")
pwd = input("Enter Password : ")
tst = web_1.login(unm,pwd)
if tst == 1:
    print("Closing the test")
else:
    print(web_1.quickresponse("Assign Leave"))
    print(web_1.quickresponse("Leave List"))
    print(web_1.quickresponse("Timesheets"))
    web_1.logout()


