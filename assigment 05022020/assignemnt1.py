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
        self.driver = webdriver.Chrome(
            executable_path="//Users/anjalinairandayil//PycharmProjects//Assignments-Anjali//drivers//chromedriver")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def logintoapp(self):
        print("Login Started")
        self.driver.find_element_by_name("txtUsername").send_keys("admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        try:
            if self.driver.find_element_by_id("welcome").is_displayed():
                print("Logged in successfully")
        except:
            print("Invalid credentials")
            return 1
        print("Login Completed")

    def assignleave(self):
        print("Assign leave Started")
        self.driver.find_element_by_css_selector(
            "img[src='/webres_5e7b15c4882d04.47780062/orangehrmLeavePlugin/images/ApplyLeave.png']").click()
        time.sleep(15)
        try:
            if (self.driver.find_element_by_id("assign-leave").is_displayed()):
                test1 = self.driver.find_element_by_xpath('//*[@id="assign-leave"]/div[1]/h1').text
                print("The header is ", test1)
        except:
            print("Text not found - try again")
        self.driver.find_element_by_id("menu_dashboard_index").click()
        try:
            if (self.driver.find_element_by_id("dashboard-quick-launch-panel-container").is_displayed()):
                print("Dashboard Page is displayed")
        except:
            print("Text not found - try again")
        print("Assign Leave Completed")

    def leavelist(self):
        print("Leave List Started")
        self.driver.find_element_by_xpath('//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[2]/div/a/span').click()
        time.sleep(15)
        try:
            if (self.driver.find_element_by_id("leave-list-search").is_displayed()):
                test2 = self.driver.find_element_by_xpath('//*[@id="leave-list-search"]/div[1]/h1').text
                print("The header is ", test2)
        except:
            print("Text not found - try again")
        self.driver.find_element_by_id("menu_dashboard_index").click()
        try:
            if (self.driver.find_element_by_id("dashboard-quick-launch-panel-container").is_displayed()):
                print("Dashboard Page is displayed")
        except:
            print("Text not found - try again")
        print("Leave list closed")

    def timesheet(self):
        print("Time sheet Started")
        self.driver.find_element_by_css_selector(
            "img[src='/webres_5e7b15c4882d04.47780062/orangehrmTimePlugin/images/MyTimesheet.png']").click()
        time.sleep(15)
        try:
            if (self.driver.find_element_by_id("employeeSelectForm").is_displayed()):
                test3 = self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/div[1]/h1').text
                print("The header is ", test3)
        except:
            print("Text not found - try again")
        self.driver.find_element_by_id("menu_dashboard_index").click()
        try:
            if (self.driver.find_element_by_id("dashboard-quick-launch-panel-container").is_displayed()):
                print("Dashboard Page is displayed")
        except:
            print("Text not found - try again")
        print("Time Sheet completed")

    def logout(self):
        print("Logout Started")
        self.driver.find_element_by_id("welcome").click()
        time.sleep(15)
        self.driver.find_element_by_xpath('//*[@id="welcome-menu"]/ul/li[2]/a').click()
        print("user logged out")
        self.driver.close()
        print("Logout Completed")


web = website()
tst = web.logintoapp()
if tst == 1:
    print("Closing the test")
else:
    web.assignleave()
    web.leavelist()
    web.timesheet()
    web.logout()
