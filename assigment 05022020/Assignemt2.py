# selenium assignment :2
# Login with Invalid Credentials and capture the login failure message


from selenium import webdriver
import time

class web():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="//Users//anjalinairandayil//PycharmProjects//Assignments-Anjali//drivers//chromedriver")
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

    def loginapp(self):
        self.driver.find_element_by_name("txtUsername").send_keys("admin11")
        print("Entered username")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        print("Entered password")
        self.driver.find_element_by_name("Submit").click()
        test = self.driver.find_element_by_xpath('//*[@id="spanMessage"]').text
        print (test)
        # try:
        #     if self.driver.find_element_by_id("welcome").is_displayed():
        #         print("Logged in successfully")
        # except:
        #     print("Invalid credentials")
        self.driver.close()


web_1 =web()
web_1.loginapp()