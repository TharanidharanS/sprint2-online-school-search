from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time
import unittest


class test2_Test(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:/Users/gmpat/Downloads/chromedriver_win32/chromedriver.exe")



    def test_schoolPage(self):

        self.driver.implicitly_wait(10)

        self.driver.get("https://www.eduvidya.com/Schools-in-India.aspx")

    def test_searchPage(self):

        select = Select(self.driver.find_element(by=By.NAME, value="ctl00$cp_left$ddl_Category"))
        select.select_by_visible_text("International School")

        select = Select(self.driver.find_element(by=By.NAME, value="ctl00$cp_left$ddl_City"))

        select.select_by_visible_text("Hyderabad")
        self.assertTrue(True)

        self.driver.find_element(by=By.XPATH, value="//input[@id='btnSearch']").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test has been Completed")


if __name__ == "__main__":
    unittest.main()


