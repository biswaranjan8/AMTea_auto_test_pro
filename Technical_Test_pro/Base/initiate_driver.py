from selenium.webdriver import Chrome


def startBrowser():
    driver = Chrome(executable_path="../Driver/chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver