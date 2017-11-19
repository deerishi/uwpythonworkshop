from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import selenium
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options
_chrome_options = Options()
_chrome_options.add_argument('disable-infobars')
driver = webdriver.Chrome(executable_path='/home/drishi/CoolStuffinPython/chromedriver',chrome_options=_chrome_options)

#driver=webdriver.Firefox()
driver.get("http://www.google.com")
inputelement=driver.find_element_by_name("q")

f=open('names.txt','r')
names=[]
for line in f:
    names.append(line.split('\n')[0])
count=0
for name in names:
    print 'Name is ',name
    inputelement=driver.find_element_by_name("q")
    inputelement.send_keys(name)
    inputelement.submit()
    time.sleep(5)
    count=count+1
    if count<len(names):
        inputelement=driver.find_element_by_name("q")
        inputelement.clear()
time.sleep(10)
driver.quit()
