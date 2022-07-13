import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class test_login_page(unittest.TestCase):
    '''This is login page'''

    def __init__(self, driver):
        super().__init__()
        self.driver=driver
        self.username_name="userName"
        self.password_name="password"
        self.login_btn="submit"

    def enter_username(self,username):
        self.driver.find_element(by=By.NAME,value=self.username_name).send_keys(username)
    def enter_pwd(self,pwd):
        self.driver.find_element(by=By.NAME,value=self.password_name).send_keys(pwd)
    def submit(self):
        self.driver.find_element(by=By.NAME,value=self.login_btn).click()


