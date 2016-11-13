import time
import requests
import smtplib
import re
from lxml import html

BASE_URL ="http://www.ebay.ca/itm/BabylissPRO-Miracurl-Pro-Auto-Curl-Machine-/111888749864?&_trksid=p2056016.m2518.l4276"
r = requests.get(BASE_URL)
tree = html.fromstring(r.text)
XPATH_SELECTOR = '//*[@id="prcIsum"]'
print 'code is ',r.status_code,' and text is ',tree.text
str1=re.search('\d+.\d+$',tree.xpath(XPATH_SELECTOR)[0].text[1:])

print 'str1 is ',str1.group(0)
