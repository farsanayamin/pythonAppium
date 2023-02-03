from appium import webdriver
from selenium.webdriver.common.by import By

desired_caps = {}
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '13'
desired_caps['deviceName'] = 'Pixel 4 XL API 33'
desired_caps['app'] = r'C:\Users\ksaje\Downloads\com.simplemobiletools.filemanager_3.4.0-50_minAPI16(nodpi)_apkmirror.com.apk'
#desired_caps['app'] = r'C:\Users\ksaje\Downloads\instagram-265-0-0-19-301.apk'

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
