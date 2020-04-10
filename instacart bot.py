from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
##driver = webdriver.Firefox(executable_path=r'geckodriver.exe')


import smtplib

loginPasssword = "password"
loginUser = "username"
emailUser = "email"
emailPassword = "get_from_app_passwords_google" # get password by setting up app passwords on google

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--window-position=0,0 --window-size=1,1')
dir_path = os.path.dirname(os.path.realpath(__file__))
chromedriver = dir_path + "/chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(options = options, executable_path = chromedriver)
driver.get("https://www.instacart.com/")
#Authentication
time.sleep(5)
loginButton = driver.find_element_by_xpath('/html/body/main/div[1]/div/div/div/div/header/div/div[2]/div/button');
loginButton.click()

time.sleep(5)
userName = driver.find_element_by_id('nextgen-authenticate.all.log_in_email')
time.sleep(0.5)
userName.send_keys(loginUser)

time.sleep(0.5)
passWord = driver.find_element_by_id('nextgen-authenticate.all.log_in_password')
time.sleep(0.5)
passWord.send_keys(loginPasssword + '\n')
# Checking for spot
while(True):
    time.sleep(5)
    driver.get("https://www.instacart.com/store/checkout_v3")

    time.sleep(10)
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)
    try: # First check - if spots available
        noTime = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/div/p/span[1]/span')
        strOut = noTime.text
        if(strOut != 'We’re sorry, all shoppers are busy for today.'):
            print("error")
            passWord = emailPassword
            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server_ssl.ehlo()
            server_ssl.login(emailUser , passWord)
            server_ssl.sendmail(emailUser, emailUser, "GOT SPOT")
    except: # second check - if available spots are open
        time.sleep(5)
        try:
            noTime = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/img')

        except:
            print("error2")
            passWord = emailPassword
            server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server_ssl.ehlo()
            server_ssl.login(emailUser , passWord)
            server_ssl.sendmail(emailUser, emailUser, "GOT SPOT")
    time.sleep(900) #change for faster update
    
    
