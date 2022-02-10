import selenium
from selenium import webdriver
from optparse import OptionParser
import pyautogui
import time

options=webdriver.ChromeOptions()
options.add_argument("--disable-notification")


driver=webdriver.Chrome(executable_path="D:\chromedriver_win32\chromedriver.exe",chrome_options=options)

#initialize window in fullscreen
driver.maximize_window
time.sleep(10)
driver.close()
