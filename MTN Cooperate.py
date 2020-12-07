from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


# number would be collected from user input
def login(number):
    try:
        # automated website of choice
        driver.get("https://mymtn.com.ng/")
        time.sleep(10)

        # login
        driver.find_element_by_xpath("//*[@id='mat-input-0']").send_keys(number)
        driver.find_element_by_xpath("//*[@id='label']").click()
        time.sleep(60)

        return "Login Successful"

    except:
        print("Poor internet connection")


# OTP Verification has to be done manually.

def dashboard():
    """ Searches for the appropriate subcription button and clicks it """

    try:
        driver.get("https://mymtn.com.ng/dashboard/")
        time.sleep(30)

        driver.find_element_by_xpath(
            '//*[@id="tat"]/app-dashboard/div/div[2]/div[3]/div/div/app-cards/div/div/div[2]/div[2]/button').click()
        time.sleep(30)
        driver.find_element_by_xpath('//*[@id="wht-crv"]/div/div/app-buybundle-submenu/div[1]/div/ol/li[2]').click()
        time.sleep(0.5)

    except:
        print("Poor Network Connection")


def subscribe(recipient_name, recipient_number):
    """ Chooses the cooperate data gifting plan and fills the receipient's details """
    try:
        # getting the bundle
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id='wht-crv']/div/div/app-buybundle-submenu/div[1]/div/div/div/a[8]").click()
        time.sleep(1)

        # recipient name
        driver.find_element_by_xpath(
            "//*[@id='wht-crv']/div/div/app-buybundle-submenu/div[2]/app-sponsoredwebpass/div/div[2]/div[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="mat-input-2"]').send_keys(recipient_name)

        # validity for 30days and 2GB
        time.sleep(4)
        driver.find_element_by_xpath('//*[@id="mat-radio-8"]/label/div[1]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="mat-radio-14"]').click()

        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="feedbackmsg"]').send_keys(recipient_number)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="shownxt"]/div[9]/app-mainbutton').click()

        time.sleep(20)
        driver.close()

    except:
        print("Poor Internet Connection")


# PLEASE NOTE: For the sake of this script, user variables are pre-defined
login(number="08039506623")
dashboard()
subscribe(recipient_name="mike", recipient_number="080365329")
