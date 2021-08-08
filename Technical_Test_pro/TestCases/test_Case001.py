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


@pytest.mark.usefixtures('setpath')
def test_page():
    global pgt
    pgt = Test_Page(driver)

    pgt.click_gift_link()

    driver.execute_script("window.scrollTo(0,300);")

    pgt.click_Policeman_box_link()


@pytest.mark.usefixtures('setpath')
def test_close_Alert():
    time.sleep(2)
    pgt.click_close_alrt_popup()


@pytest.mark.usefixtures('setpath')
def test_Add_basket():
    pgt.click_Add_to_tea_Basket()

    x = pgt.Sub_Total_text()
    file = open("../result/generate.txt", mode='w+')
    file.write(x)
    file.close()

    pgt.click_remove_chart_link()
    time.sleep(3)
