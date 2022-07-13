from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time
import unittest


class test3_Test(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:/Users/gmpat/Downloads/chromedriver_win32/chromedriver.exe")



    def test_schoolPage(self):

        self.driver.implicitly_wait(10)

        self.driver.get("https://www.eduvidya.com/School-Search.aspx?Category=International-School&CategoryID=10&City=Hyderabad&CityID=25")

        self.driver.find_element(By.LINK_TEXT, "Arbor International School").click()

        self.driver.maximize_window()
        self.driver.save_screenshot("D:\Anurag\Screenshot\school.png")

        time.sleep(3)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test has been Completed")


if __name__ == "__main__":
    unittest.main()
