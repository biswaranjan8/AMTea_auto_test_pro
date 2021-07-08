from Base_file.initiate_driver import startBrowser
from Pages import sign_in_page
import unittest
import time
from Data_generater import xlUtils


class sign_in_test(unittest.TestCase):
    driver = startBrowser()
    base_url = "https://opensource-demo.orangehrmlive.com/"
    path = "./Data_generater/login_valid_book.xlsx"
    rows = xlUtils.getRowCount(path, 'Sheet1')

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.base_url)
        cls.driver.implicitly_wait(10)

    def test_sign(self):
        sn = sign_in_page.SignPage(self.driver)
        for r in range(2, self.rows + 1):
            username = xlUtils.readData(self.path, 'Sheet1', r, 1)
            password = xlUtils.readData(self.path, 'Sheet1', r, 2)
            sn.SetUserName(username)
            time.sleep(0.5)
            sn.SetUserPass(password)
            time.sleep(0.5)
            sn.SetLogin()
            if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/index.php/dashboard":
                print("Test is pass")
                xlUtils.writeData(self.path, 'Sheet1', r, 3, 'pass')
                self.driver.find_element_by_xpath("//a[@id='welcome']").click()
                time.sleep(0.5)
                self.driver.find_element_by_xpath("//li/a[text()='Logout']").click()
            else:
                print("test failed")
                xlUtils.writeData(self.path, 'Sheet1', r, 3, 'failed')

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        print("Test Completed")



