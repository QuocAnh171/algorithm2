from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.remote import errorhandler

# geckodriver_autoinstaller.install()
get_data = webdriver.Chrome()
get_data.get("http://45.79.43.178/source_carts/wordpress/wp-admin/")

username = get_data.find_element_by_name('log')
username.clear()
username.send_keys('admin')
password = get_data.find_element_by_name('pwd')
password.clear()
password.send_keys('123456aA')
password.send_keys(Keys.RETURN)

sleep(10)
print(get_data.page_source)
while True:
    try:
        ten = get_data.find_element_by_class_name('display-name')
        print(ten.text)
        break
    except errorhandler.NoSuchElementException:
        continue
sleep(20)
get_data.close()



