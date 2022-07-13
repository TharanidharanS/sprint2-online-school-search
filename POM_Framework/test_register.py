import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class test_register_page(unittest.TestCase):
    '''this is registration page'''
    def __init__(self, driver):
        super().__init__()
        self.driver=driver
        self.first_name_name="firstName"
        self.last_name_name="lastName"
        self.ph_name="phone"
        self.address_name="address1"
        self.submit_name="submit"
    def enter_firstname(self,first):
        self.driver.find_element(by=By.NAME,value=self.first_name_name).send_keys(first)

    def enter_lastname(self,last):
        self.driver.find_element(by=By.NAME,value=self.last_name_name).send_keys(last)

    def enter_phone_num(self,phn):
        self.driver.find_element(by=By.NAME,value=self.ph_name).send_keys(phn)

    def enter_address(self,add):
        self.driver.find_element(by=By.NAME,value=self.address_name).send_keys(add)

    def submit_button(self):
        self.driver.find_element(by=By.NAME,value=self.submit_name).click()
