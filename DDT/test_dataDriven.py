from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyexcel
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="C:/Users/tharun/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
sheet = openpyexcel.load_workbook("C:/Users/tharun/OneDrive/Documents/demo.xlsx")
book = sheet.active
r = book.max_row
for i in range(2, r + 1):
    username = book.cell(row=i, column=1).value
    password = book.cell(row=i,column=2).value
    print(username,password)
    driver.find_element(by=By.XPATH,value="//input[@id='txtUsername']").send_keys(username)
    driver.find_element(by=By.XPATH,value="//input[@id='txtPassword']").send_keys(password)
    driver.find_element(by=By.XPATH,value="//input[@id='btnLogin']").click()
    time.sleep(3)

    driver.get("https://opensource-demo.orangehrmlive.com/")

