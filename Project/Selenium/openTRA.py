from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime')

# 出發站 icon

browser.find_element_by_xpath('//*[@id="queryForm"]/div/div[1]/div[2]/div[2]/button[1]').click()

# 出發站 縣市 台中市

browser.find_element_by_xpath('//*[@id="mainline"]/div[1]/ul/li[9]/button').click()

# 出發站 站名 臺中

browser.find_element_by_xpath('//*[@id="city66000"]/ul/li[18]/button').click()

# 抵達站 icon

browser.find_element_by_xpath('//*[@id="queryForm"]/div/div[1]/div[4]/div[2]/button[1]').click()

# 抵達站 縣市 臺北市

browser.find_element_by_xpath('//*[@id="mainline"]/div[1]/ul/li[4]/button').click()

# 抵達站 站名 臺北

browser.find_element_by_xpath('//*[@id="city63000"]/ul/li[3]/button').click()

# find 查詢

browser.find_element_by_name('query').click()