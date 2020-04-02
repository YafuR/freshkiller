import os
import random
import time

import bs4
from selenium import webdriver
import util

auto_log = 1


def freshkiller_s(url):
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get(url)
    soup = bs4.BeautifulSoup(driver.page_source,'html.parser')
    if not auto_log:
        time.sleep(45)
    else:
        util.auto_login(driver)
    #add auto login
    no_slots = True
    n = 0
    availibility = False
    start_time = time.time()
    while no_slots:
        n+=1
        driver.refresh()
        soup = bs4.BeautifulSoup(driver.page_source, 'html.parser')
        warning_sentence = soup.find_all('h4',class_ = 'a-alert-heading')
        if len(warning_sentence) != 3:
            availibility = True
            no_slots = False
        for sentence in warning_sentence:
            if "No delivery windows available" not in str(sentence):
                print(sentence)
                availibility = True
                no_slots = False
        if availibility:
            print("FOUND")
            for i in range(10):
                os.system('say "Slots Founded"')
            time.sleep(3600)
        time.sleep(random.randint(1,10))
        print(str(n) + "st try, run time:" + str(time.time() - start_time))

if __name__ == '__main__':
    url = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcart%2Fview.html%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
    freshkiller_s(url)
