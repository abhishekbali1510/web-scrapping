from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.youtube.com/watch?v=P-DhwN87JDY')
time.sleep(5)
print("hey")

search = browser.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string')
print(search.text)
search = browser.find_element_by_xpath('//*[@id="description"]')
print(search.text)