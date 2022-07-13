import time
import openpyexcel
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



@given(u'user in eduvidya website')
def launch_driver(context):
    # ------------------------------------------------- Launching chrome webdriver-------------------

    context.driver = webdriver.Chrome(executable_path="C:/Users/shubham/Downloads/chromedriver_win32/chromedriver.exe")
    global driver
    driver = context.driver
    global sheet
    sheet = openpyexcel.load_workbook("C:\\Users\\shubham\\OneDrive\\Desktop\\python practice\\eduvidya status.xlsx")
    global book
    book = sheet.active


@when(u'user click on school')
def click_schools(context):
    # ----------- --------------------------------------Opening the eduvidya website-----------------

    driver.get("https://www.eduvidya.com/")
    driver.maximize_window()
    window_before = driver.window_handles[0]

    # ---------- ----------------------------------------Verifying the eduvidya website-------------
    title = driver.title

    #----------- assert method could also be used-----------------------

    # assert "Colleges|Schools|Universities|Exams|Courses|Distance Education|India|Eduvidya.com|" in titleh5
    if "Colleges|Schools|Universities|Exams|Courses|Distance Education|India|Eduvidya.com|"==title:
        book.cell(row=2, column=2).value='PASS'
    else:
        book.cell(row=2, column=2).value = 'FAIL'
    sheet.save("C:\\Users\\shubham\\OneDrive\\Desktop\\python practice\\eduvidya status.xlsx")


    # ------------------------------------------------- Clicking on Schools--------------------

    driver.find_element_by_xpath("//body/div[@id='container']/div[1]/div[2]/ul[1]/li[4]/a[1]").click()

    # ---------------- wait until new window is loading--------------
    global wait
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//select[@id='ddl_Category']")))

    # ---------------------------------------------------Switching to schools window-------------------

    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)
    global title1
    title1 = driver.title


@when(u'user search for school board and location and click on search')
def select_board_location(context):
    #assert "Best Schools in India 2022 List, Top Ranking CBSE, ICSE, IB schools" in title1
    if "Best Schools in India 2022 List, Top Ranking CBSE, ICSE, IB schools"==title1:
        book.cell(row=3, column=2).value = 'PASS'
    else:
        book.cell(row=3, column=2).value = 'FAIL'
    sheet.save("C:\\Users\\shubham\\OneDrive\\Desktop\\python practice\\eduvidya status.xlsx")

    # --------------------------------------------------------------- Selecting board-----------------------------

    board = Select(driver.find_element_by_xpath("//select[@id='ddl_Category']"))
    board.select_by_index(3)

    # --------------------------------------------------------------- Selecting location---------------------------

    location = Select(driver.find_element_by_xpath("//select[@id='ddl_City']"))
    location.select_by_visible_text("Pune")

    # --------------------------------------------------------------- Clicking on search button----------------------

    driver.find_element_by_xpath("//input[@id='btnSearch']").click()
    global title2
    title2 = driver.title


@then(u'user get the school details and user verifies it')
def verifying_opened_page(context):
    # -----------------------------------------------------------------verifying the searched page----------------------

    #assert "Best Schools in India 2013, List, Ranking" in title2
    if "Best Schools in India 2022 List, Top Ranking CBSE, ICSE, IB schools"==title1:
        book.cell(row=4, column=2).value = 'PASS'
    else:
        book.cell(row=4, column=2).value = 'FAIL'
    sheet.save("C:\\Users\\shubham\\OneDrive\\Desktop\\python practice\\eduvidya status.xlsx")


@when(u'user screenshots 3 the available schools')
def screenshots(context):
    pass
    # ------------------------------------------------------------Screenshots--------------------------

    element = driver.find_element_by_xpath("//*[@id='pnllist']/div[2]/ul/li[4]/div[1]/img")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='pnllist']/div[2]/ul/li[2]/div[1]/img")))
    driver.save_screenshot('C:/Users/shubham/PycharmProjects/eduvidya_sprint2/pom/screenshots/image1.png')

    driver.execute_script("window.scrollBy(150,400)", " ")
    time.sleep(3)
    driver.save_screenshot("C:/Users/shubham/PycharmProjects/eduvidya_sprint2/pom/screenshots/image2.png")

    element2 = driver.find_element_by_xpath("//*[@id='pnllist']/div[2]/ul/li[15]/div[2]/a")
    driver.execute_script("arguments[0].scrollIntoView();", element2)
    wait.until(ec.visibility_of_element_located((By.XPATH, "//*[@id='pnllist']/div[2]/ul/li[12]/div[1]/img")))
    driver.save_screenshot("C:/Users/shubham/PycharmProjects/eduvidya_sprint2/pom/screenshots/image3.png")


# -----------------------------------------------Closing the browser-----------------------
@when(u'user close the driver')
def step_impl(context):
    driver.close()

# ----    behave -f allure_behave.formatter:AllureFormatter -o reports    -----
# this command is used to generate reports

# ---    allure serve reports   --
# this command convert json reports into html reports

