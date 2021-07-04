from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

chrome_options = webdriver.ChromeOptions()
prefs = {
	"profile.managed_default_content_settings.images": 2
}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome('./chromedriver', options = chrome_options)

'''
driver.get('https://thangit.net/')
#jsselect = 'document.querySelector(".read-more").click()'
#driver.execute_script(jsselect)
#driver.find_element_by_css_selector('.read-more').click()
list_ele = driver.find_elements_by_css_selector('.read-more')
len(list_ele)
list_ele[3].click()
'''
driver.get('https://google.com')
input_search = driver.find_element_by_css_selector('input[name="q"]')
input_search.send_keys('thang dep trai')
