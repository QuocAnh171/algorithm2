from selenium import webdriver
import geckodriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from time import sleep

geckodriver_autoinstaller.install()
url = "http://45.79.43.178/source_carts/wordpress/wp-admin"
driver = webdriver.Firefox()
driver.get(url)

username = driver.find_element_by_name('log')
username.send_keys('admin')
password = driver.find_element_by_name('pwd')
password.send_keys('123456aA')
password.send_keys(Keys.RETURN)

sleep(20)

name = driver.find_element_by_class_name("dislay_name")
print(name.text)

