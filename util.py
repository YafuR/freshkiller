import time
import random
def auto_login(driver):
    f = open('login_info.txt')
    info = []
    for item in f:
        info.append((item))
    email = driver.find_element_by_xpath("//*[@id=\"ap_email\"]")
    time.sleep(random.randint(1, 3))
    email.send_keys(info[0])
    time.sleep(random.randint(1,3))
    password = driver.find_element_by_xpath("//*[@id=\"ap_password\"]")
    password.send_keys(info[1])
    time.sleep(random.randint(1, 3))
    login_button = driver.find_element_by_xpath("//*[@id=\"signInSubmit\"]")
    login_button.click()
    time.sleep(random.randint(1, 3))
    checkout_button = driver.find_element_by_xpath("//*[@id=\"sc-alm-buy-box-ptc-button-QW1hem9uIEZyZXNo\"]/span/input")
    checkout_button.click()
    time.sleep(random.randint(1, 2))
    continue_button = driver.find_element_by_xpath("//*[@id=\"a-autoid-0\"]")
    continue_button.click()
    #time.sleep(1000)


