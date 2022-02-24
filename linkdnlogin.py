import selenium
from selenium import webdriver
from optparse import OptionParser
import pyautogui
import time
from bs4 import BeautifulSoup

options=webdriver.ChromeOptions()
options.add_argument("--disable-notification")


driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe",chrome_options=options)

#initialize window in fullscreen
#driver.maximize_window
#time.sleep(10)
#driver.close()

driver.get("https://www.linkedin.com/uas/login")

file = open('cred.txt')
creds = file.readlines()
username = creds[0]
pswd = creds[1]


#getting credentials for login
elemID = driver.find_element_by_id('username')
elemID.send_keys(username)

elemID = driver.find_element_by_id('password')
elemID.send_keys(pswd)


elemID.submit()

myprofile = '/in/kartikey-gautam711'
url = 'https://www.linkedin.com'  +myprofile
driver.get(url)

profilestovisit = []

def visitprofile(profilestovisit):
    server_profiles = open('users.txt')
    for profile in server_profiles:
        profilestovisit.append(profile.strip())
    return profilestovisit

    


