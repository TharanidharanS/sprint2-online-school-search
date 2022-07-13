import time
import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from POM.pages.login_page import test_login_page
from POM.pages.register_page import test_register_page

class test_webtours(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:/Users/shubham/Downloads/chromedriver_win32/chromedriver.exe")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_webtour(self):
        driver=self.driver
        driver.get("https://demo.guru99.com/test/newtours/")
        login = test_login_page(driver)
        login.enter_username("Ajay")
        time.sleep(2)
        login.enter_pwd('sharma')
        time.sleep(2)


    def test_register_webtour(self):
        driver=self.driver
        driver.get("https://demo.guru99.com/test/newtours/register.php")
        register = test_register_page(driver)
        register.enter_firstname('Ajay')
        register.enter_lastname('sharma')
        register.enter_phone_num('123456')
        register.enter_address("123,abc,xyz lane")
        register.submit_button()
        wait = WebDriverWait(driver,10)
        element = driver.find_element(by=By.XPATH,value="//tbody/tr[1]/td[1]/p[3]/img[1]")
        driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        wait.until(ec.visibility_of_element_located((By.XPATH,'//tbody/tr[1]/td[1]/p[3]/img[1]')))

        driver.get_screenshot_as_file('C:/Users/shubham/PycharmProjects/pom/POM/Reports/image1.png')

if __name__=="__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/shubham/PycharmProjects/pom/POM/Reports.html'))
    
