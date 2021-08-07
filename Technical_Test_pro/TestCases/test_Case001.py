from Base.initiate_driver import startBrowser
from Pages.page_obj import Test_Page
import pytest
import time


@pytest.fixture(scope='module')
def setpath():
    global driver
    driver = startBrowser()
    driver.get("https://ahmadteausa.com/")

    yield
    driver.close()


def test_page(setpath):
    pgt = Test_Page(driver)
    pgt.click_gift_link()

    driver.execute_script("window.scrollTo(0,300);")

    pgt.click_Policeman_box_link()
    time.sleep(3)
    pgt.click_close_alrt_popup()
    driver.execute_script("window.scrollTo(0,100);")
    time.sleep(3)
    pgt.click_Add_to_tea_Basket()
    time.sleep(3)

    x = pgt.Sub_Total_text()
    file = open("../result/generate.txt", 'w')
    file.write(x)
    file.close()

    time.sleep(2)
    pgt.click_remove_chart_link()
    time.sleep(3)
