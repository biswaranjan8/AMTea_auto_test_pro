"""Demo purpose"""
from selenium.webdriver import Chrome
from Data_generater import xlUtils
import time

driver = Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.implicitly_wait(10)
driver.maximize_window()

path = "C:\\Users\\Admin\\PycharmProjects\\data_driven_pom_excel\\Data_generater\\login_valid_book.xlsx"
rows = xlUtils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    username = xlUtils.readData(path,'Sheet1',r,1)
    password = xlUtils.readData(path,'Sheet1',r, 2)
    driver.find_element_by_name("txtUsername").send_keys(username)
    time.sleep(0.5)
    driver.find_element_by_name("txtPassword").send_keys(password)
    time.sleep(0.5)
    driver.find_element_by_name("Submit").click()
    time.sleep(1)

    if driver.current_url == "https://opensource-demo.orangehrmlive.com/index.php/dashboard":
        print("Test is pass")
        xlUtils.writeData(path,'Sheet1',r,3,'pass')
        driver.find_element_by_xpath("//a[@id='welcome']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//li/a[text()='Logout']").click()
    else:
        print("test failed")
        xlUtils.writeData(path,'Sheet1',r,3,'failed')
driver.close()
