from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS

url ="https://bidplus.gem.gov.in/bidlists"

browser = webdriver.Chrome("C:\Users\kushal\Downloads/chromedriver_win32/chromedriver.exe")
browser.get(url)

BID_no= browser.find_element_by_name("treg")
BID_no.open 



