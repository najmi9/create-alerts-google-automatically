#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
Created on Tusday Oct 6 10:54:42 2020

@author: Najmi Imad
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

url1 = "https://google.com/alerts"
url2 = " https://stackoverflow.com/users/login"

email = "@gmail.com"
password = "****"
alert = "Web-Scraping"

options = Options()
options.headless=False

options.add_argument('--disable-web-security')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--enable-automation')
#options.add_argument('--user-data-dir')
options.add_argument('--disable-extensions')

options.add_argument('--profile-directory=Default')

options.add_argument("--incognito")

options.add_argument("--disable-plugins-discovery")


driver = webdriver.Chrome('../chromedriver', options=options)

driver.get(url2)
sleep(2)

driver.find_element_by_xpath('//button[@data-provider="google"]').click()
sleep(2)

driver.find_element_by_xpath('//input[@type="email"]').send_keys(email) 
driver.find_element_by_css_selector('div.VfPpkd-RLmnJb').click()
sleep(2)

wait = WebDriverWait(driver, 10)
input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))
sleep(5)
ActionChains(driver).send_keys(password).perform()
sleep(2)
driver.find_element_by_css_selector('div.VfPpkd-RLmnJb').click()

sleep(3)
driver.get(url1)
sleep(2)

inp = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))
inp.send_keys(alert)

inp = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span#create_alert')))
inp.click()
driver.close()
driver.quit()

