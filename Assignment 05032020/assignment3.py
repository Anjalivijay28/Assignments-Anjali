# Navigatre to below page and extract the fieldNames and their corresponding input values
# https://opensource-demo.orangehrmlive.com/index.php/admin/viewOrganizationGeneralInformation


from selenium import webdriver
import time
import itertools

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

    def all_elements(self):
        self.driver.find_element_by_id("menu_admin_viewAdminModule").click()
        time.sleep(3)
        self.driver.find_element_by_id("menu_admin_Organization").click()
        time.sleep(5)
        self.driver.find_element_by_id("menu_admin_viewOrganizationGeneralInformation").click()
        print("Form print started")
        try:
            if (self.driver.find_element_by_id("genInfoHeading").is_displayed()):
                time.sleep(5)
                test= self.driver.find_elements_by_xpath("//form[@id='frmGenInfo']//li//label")
                test2 = self.driver.find_elements_by_xpath("//form[@id='frmGenInfo']//li//input | //form[@id='frmGenInfo']//li//span | //form[@id='frmGenInfo']//li//textarea | //form[@id='frmGenInfo']//li//select")
                for (i,j) in itertools.zip_longest(test, test2):
                    print (i.text)
                    if (j.tag_name== "input"):
                        print(j.get_attribute("value"))
                    elif (j.tag_name== "textarea"):
                        print(j.text)
                    elif (j.tag_name == "span"):
                        print(j.text)
                    elif (j.tag_name == "select"):
                        z = self.driver.find_elements_by_xpath("//form[@id='frmGenInfo']//li//select//option")
                        for a in z:
                            if (a.get_attribute("selected") == 'true'):
                                print(a.text)

        except:
            print ("Invalid scenario")
        print("Form print Ended")


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
        self.driver.close()



web_1 = website()
unm = input("Enter user Name : ")
pwd = input("Enter Password : ")
tst = web_1.login("unm","pwd")
if tst == 1:
    print("Closing the test")
else:
    # print(web_1.quickresponse("Assign Leave"))
    # print(web_1.quickresponse("Leave List"))
    # print(web_1.quickresponse("Timesheets"))
    web_1.all_elements()
    web_1.logout()


