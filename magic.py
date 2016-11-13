from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import selenium
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path='/home/drishi/CoolStuffinPython/geckodriver')

#driver=webdriver.Firefox()
driver.get("http://www.google.com")
inputelement=driver.find_element_by_name("q")

f=open('names.txt','r')
names=[]
for line in f:
    names.append(line.split('\n')[0])
count=0
for name in names:
    inputelement.send_keys(name)
    inputelement.submit()
    time.sleep(5)
    count=count+1
    if count<len(names):
        inputelement.clear()
time.sleep(10)
driver.quit()
