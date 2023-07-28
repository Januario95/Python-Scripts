# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:38:50 2022

@author: a248433
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\\Users\\a248433\\Documents\\drivers\\chromedriver.exe')
driver.get("http://localhost:8000/register")
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

