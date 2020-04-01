import random
import bs4
from selenium import webdriver
import os
import time

def freshkiller_s(url):
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.get(url)
    soup = bs4.BeautifulSoup(driver.page_source,'html.parser')
    time.sleep(45)
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
        time.sleep(random.randint(1,5))
        print(str(n) + "st try, run time:" + str(time.time() - start_time))

if __name__ == '__main__':
    url = "https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1"
    freshkiller_s(url)
