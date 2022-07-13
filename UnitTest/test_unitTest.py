from selenium import webdriver
import HtmlTestRunner
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest , time
import HtmlTestRunner



def setUpModule():
    print("SetUp Module")


def tearDownModule():
    print("TearDown Module")


class Search_Google(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Users/vaibhav/OneDrive/Desktop/selenium/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_HomePageTitle(self):
        self.driver.get("https://www.eduvidya.com/")
        print(self.driver.title)
        # assert self.driver.title == "Colleges|Schools|Universities|Exams|Courses|Distance Education|India|Eduvidya.com|"
        self.assertEqual(self.driver.title, "Colleges|Schools|Universities|Exams|Courses|Distance Education|India|Eduvidya.com|")

    def test_Search_School(self):
        driver = self.driver
        driver.get("https://www.eduvidya.com/")
        driver.maximize_window()
        print("Title of page", driver.title)
        driver.find_element_by_link_text("Schools").click()
        driver.find_element_by_id("ddl_Category").click()
        Select(driver.find_element_by_id("ddl_Category")).select_by_visible_text("CBSE")
        driver.find_element_by_id("ddl_City").click()
        Select(driver.find_element_by_id("ddl_City")).select_by_visible_text("Pune")
        driver.find_element_by_id("btnSearch").click()
        time.sleep(5)

        driver.save_screenshot("C:\\Users\\vaibhav\\PycharmProjects\\pythonProject\\seleniumproject\\screenshots\\flight1.png")
        driver.execute_script("window.scrollBy(0,750)", " ")
        time.sleep(3)

    @classmethod
    def tearDown(self):
        self.driver.close()

    @classmethod
    def setUpClass(cls):
        print("Application Started")

    @classmethod
    def tearDownClass(cls):
        print("Close Application")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\vaibhav\\PycharmProjects\\pythonProject\\seleniumproject\\HtmlReport'))

