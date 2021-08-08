from Library.read_config_elements import conf_ele_read
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Test_Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def gift_link(self):
        """It will click Gift link"""
        gft = self.driver.find_element_by_xpath(conf_ele_read('element_section', 'gift_link_xpath'))
        return gft

    def Policeman_box_link(self):
        """It will Policeman Box"""
        pol = self.driver.find_element_by_xpath(conf_ele_read('element_section', 'Policeman_box_xpath'))
        return pol

    def close_alrt_popup(self):
        """It will Close Popup"""
        alrt = self.driver.find_element_by_xpath(conf_ele_read('element_section', 'close_alrt_popup_xpath'))
        return alrt

    def Add_to_tea_Basket(self):
        """It will Add to basket item"""
        add = self.driver.find_element_by_xpath(conf_ele_read('element_section', 'Add_to_tea_Basket_xpath'))
        return add

    def Sub_Total_text(self):
        """It will select Sub total Amount and By Using explicit wait"""
        sub_Total_wait = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, conf_ele_read('element_section', 'Sub_Total_xpath'))))

        return sub_Total_wait.text

    def remove_chart_link(self):
        """It will remove chart"""
        chart = self.driver.find_element_by_xpath(conf_ele_read('element_section', 'remove_chart_xpath'))
        return chart

    ################## Operation #######################

    def click_gift_link(self):
        self.gift_link().click()

    def click_Policeman_box_link(self):
        self.Policeman_box_link().click()

    def click_close_alrt_popup(self):
        self.close_alrt_popup().click()

    def click_Add_to_tea_Basket(self):
        self.Add_to_tea_Basket().click()

    def click_remove_chart_link(self):
        self.remove_chart_link().click()
