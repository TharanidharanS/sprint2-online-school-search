from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time
import pytest

class Test_global:
    driver = None


def test_Sample():
    s=Service("C:/Users/gmpat/Downloads/chromedriver_win32/chromedriver.exe")
    Test_global.driver=webdriver.Chrome(service=s)
    Test_global.driver.implicitly_wait(50)
    Test_global.driver.set_page_load_timeout(70)
    Test_global.driver.get("https://www.eduvidya.com/")
    title = Test_global.driver.title
    print("The Title of the page is:" + title)
    #assert Test_global.driver.title=="Colleges|Schools|Universities|Exams|Courses|Distance Education|India|Eduvidya.com|"
    #print("The Title Of Page Is :"+Test_global.driver.title)

    Test_global.driver.find_element(By.LINK_TEXT, "Schools").click()

    select = Select(Test_global.driver.find_element(by=By.NAME, value="ctl00$cp_left$ddl_Category"))
    select.select_by_visible_text("International School")

    select = Select(Test_global.driver.find_element(by=By.NAME, value="ctl00$cp_left$ddl_City"))

    select.select_by_visible_text("Hyderabad")


def test_Sample2():
    Test_global.driver.find_element(by=By.XPATH, value="//input[@id='btnSearch']").click()

    Test_global.driver.implicitly_wait(50)
    Test_global.driver.set_page_load_timeout(70)

    Test_global.driver.find_element(By.LINK_TEXT, "Arbor International School").click()

    Test_global.driver.maximize_window()
    Test_global.driver.save_screenshot("D:\Anurag\Screenshot\school.png")

    time.sleep(3)






