from Library.read_config_elements import conf_ele_read


class Test_Page:

    def __init__(self, driver):
        self.driver = driver

    def gift_link(self):
        """It will click Gift link"""
        return self.driver.find_element_by_xpath(conf_ele_read('element_section', 'gift_link_xpath'))

    def Policeman_box_link(self):
        """It will Click Policeman Box"""
        return self.driver.find_element_by_xpath(conf_ele_read('element_section', 'Policeman_box_xpath'))

    def close_alrt_popup(self):
        """It will Close Popup"""
        return self.driver.find_element_by_xpath(conf_ele_read('element_section', 'close_alrt_popup_xpath'))

    def Add_to_tea_Basket(self):
        """It will Add to basket item"""
        return self.driver.find_element_by_xpath(conf_ele_read('element_section', 'Add_to_tea_Basket_xpath'))

    def Sub_Total_text(self):
        """It will select Sub total Amount"""
        return self.driver.find_element_by_xpath(conf_ele_read('element_section', 'Sub_Total_xpath')).text

    def remove_chart_link(self):
        """It will remove chart"""
        return self.driver.find_element_by_xpath(conf_ele_read('element_section', 'remove_chart_xpath'))

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
