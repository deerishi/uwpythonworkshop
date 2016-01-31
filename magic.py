from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Firefox()
driver.get("http://www.google.com")
inputelement=driver.find_element_by_name("q")
inputelement.send_keys("University of Waterloo Python Workshop mentors")
inputelement.submit()
button=driver.find_elements_by_class_name("searchbutton")
inputelement.send_keys(Keys.RETURN)
time.sleep(5)
inputelement.clear()
inputelement.send_keys(" Ivana Kajic")
inputelement.submit()
time.sleep(4)
inputelement.clear()
inputelement.send_keys("Sean Aubin")
inputelement.submit()
time.sleep(5)
inputelement.clear()
inputelement.send_keys("Alan Tsang University of Waterloo")
inputelement.submit()
time.sleep(5)
inputelement.clear()
inputelement.send_keys("Sajed Haque University of Waterloo")
inputelement.submit()
time.sleep(5)
inputelement.clear()
inputelement.send_keys(" Mariah Martin Shein University of Waterloo")
inputelement.submit()
time.sleep(5)
inputelement.clear()
inputelement.send_keys(" Irish Medina University of Waterloo")
inputelement.submit()
time.sleep(10)


driver.quit()

    

