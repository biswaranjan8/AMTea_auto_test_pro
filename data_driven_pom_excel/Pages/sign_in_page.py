from Library.read_confi_element import conf_ele_read

class SignPage:

    def __init__(self, driver):
        self.driver = driver

    def SetUserName(self, UserName):
        self.driver.find_element_by_name(conf_ele_read('section1','id_by_name')).send_keys(UserName)

    def SetUserPass(self, Userpass):
        self.driver.find_element_by_name(conf_ele_read('section1','pass_by_name')).send_keys(Userpass)

    def SetLogin(self):
        self.driver.find_element_by_name(conf_ele_read('section1','login_by_name')).click()
