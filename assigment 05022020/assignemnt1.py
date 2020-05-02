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
        self.driver=webdriver.Chrome(executable_path="//Users/anjalinairandayil//PycharmProjects//Assignments-Anjali//drivers//chromedriver")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def logintoapp(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_name("txtUsername").send_keys("admin")
        print("Entered username")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        try:
            if self.driver.find_element_by_id("welcome").is_displayed():
                print("Logged in successfully")
        except:
            print("Invalid credentials")

    def assignleave(self):
        self.driver.find_element_by_css_selector("img[src='/webres_5e7b15c4882d04.47780062/orangehrmLeavePlugin/images/ApplyLeave.png']").click()
        time.sleep(10)
        try:
            if (self.driver.find_element_by_id("assign-leave").is_displayed()):
                print("Assign Leave Page is displayed ")
        except:
            print("Text not found - try again")
        self.driver.find_element_by_id("menu_dashboard_index").click()
        try:
            if (self.driver.find_element_by_id("dashboard-quick-launch-panel-container").is_displayed()):
                print("Dashboard Page is displayed")
        except:
            print("Text not found - try again")

    def leavelist(self):
        self.driver.find_element_by_css_selector("img[src='/webres_5e7b15c4882d04.47780062/orangehrmLeavePlugin/images/MyLeave.png']").click()
        time.sleep(10)
        try:
            if (self.driver.find_element_by_id("leave-list-search").is_displayed()):
                print("Leave list page is displayed")
        except:
            print("Text not found - try again")
        self.driver.find_element_by_id("menu_dashboard_index").click()
        try:
            if (self.driver.find_element_by_id("dashboard-quick-launch-panel-container").is_displayed()):
                print("Dashboard Page is displayed")
        except:
            print("Text not found - try again")

    def timesheet(self):
        self.driver.find_element_by_css_selector("img[src='/webres_5e7b15c4882d04.47780062/orangehrmTimePlugin/images/MyTimesheet.png']").click()
        time.sleep(10)
        try:
            if (self.driver.find_element_by_id("employeeSelectForm").is_displayed()):
                print("Timesheet page is displayed")
        except:
            print("Text not found - try again")
        self.driver.find_element_by_id("menu_dashboard_index").click()
        try:
            if (self.driver.find_element_by_id("dashboard-quick-launch-panel-container").is_displayed()):
                print("Dashboard Page is displayed")
        except:
            print("Text not found - try again")

    def logout(self):
        self.driver.find_element_by_id("welcome").click()
        time.sleep(10)
        self.driver.find_element_by_link_text("Logout").click()
        print("user logged out")
        self.driver.close()



web = website()
web.logintoapp()
web.assignleave()
web.leavelist()
web.timesheet()
web.logout()
