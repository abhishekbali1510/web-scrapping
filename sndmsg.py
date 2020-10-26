from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
browser.get('https://web.whatsapp.com/')
print("Enter name")
nm=input()
srch= browser.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
srch.click()
srch.send_keys(nm)
srch.send_keys(Keys.ENTER)
print("Enter msg")

x=input()

i=5
while i>0:
    msg= browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg.click()
    msg.send_keys(x)
    btn= browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
    btn.click()
    i=i-1


