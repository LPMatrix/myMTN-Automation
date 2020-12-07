
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager


# chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(ChromeDriverManager().install())


# automated website of choice
def login(number):
    try:
        driver.get("https://mymtn.com.ng/")
        time.sleep(30)

        # login
        driver.find_element_by_xpath("//*[@id='mat-input-0']").send_keys(number)
        driver.find_element_by_xpath("//*[@id='label']").click()
        time.sleep(70)
        return "Login Successful"

    except:
        print("Incorrect login details or poor internet connection")


# OTP Verification would be done manually(to be automated)
def handleOTP():
    driver.find_element_by_xpath('//*[@id="tat"]/app-login/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div/app-mainbutton').click()

    otp = input("Enter OTP: ")
    time.sleep(30)
    driver.find_element_by_xpath('//*[@id="mat-input-3"]').send_keys(otp)
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="tat"]/app-login/div/div[2]/div/div/div/div/form/div/div[2]/div/app-mainbutton').click()



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


def subscribe_SME():

    """ Chooses the subscription plan. PLEASE NOTE: THIS SCRIPT ONLY SUBSCRIBES TO 3.5GB FOR #2,500. More
    modification would be done in the future. """

    #try:
    driver.find_element_by_xpath('//*[@id="wht-crv"]/div/div/app-buybundle-submenu/div[1]/div/div/div/a[7]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="wht-crv"]/div/div/app-buybundle-submenu/div[2]/app-smebundles/div[2]/div[1]/div[2]').click()
    time.sleep(10)

    #clicking 500MB
    driver.find_element_by_xpath('//*[@id="mat-radio-16"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="mat-input-9"]').send_keys("08037168316")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="mat-input-10"]').send_keys("9890")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="wht-crv"]/div/div/app-buybundle-submenu/div[2]/app-smebundles/div[2]/div[2]/form/div[3]/div[3]/app-mainbutton').click()

    time.sleep(20)
        #driver.close()

    # except:
    #     print("Poor internet connection")


login(number='07037105968')
#handleOTP()
dashboard()
subscribe_SME()

# '07037105968' Mr KB's number

# 9890 PIN
