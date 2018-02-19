from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys

# Replace below path with the absolute path
# to chromedriver in your computer
driver = webdriver.Chrome('./chromedriver')

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = '"Akshay Wd"'

# Replace the below string with your own message
string = sys.argv[1]

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
	By.XPATH, x_arg)))
group_title.click()
#inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
#input_box = wait.until(EC.presence_of_element_located((
#	By.XPATH, inp_xpath)))


version = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]


#message = divs = driver.find_element_by_class_name('pluggable-input-body copyable-text selectable-text')
version.send_keys(string)

sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/button')[0]
sendbutton.click()
#for i in range(100):
#  print(string)
#  input_box.send_keys(string + Keys.ENTER)
#  time.sleep(1)

driver.close()

