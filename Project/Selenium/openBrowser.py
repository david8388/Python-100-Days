
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://google.com/')

el = browser.find_element_by_name('q')

el.send_keys('IT Help')

el.submit()
