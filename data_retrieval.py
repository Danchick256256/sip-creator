from tools.password import create_pass
from tools.colors import FG, RESET_ALL, BOLD
from tools.text import cant_find_element
from tools.clear_console import clear_console

from selenium.common.exceptions import NoSuchElementException


def data_retrieval(starting_flat, driver):
    try:
        driver.find_element_by_xpath("/html/body/div/div/div/a").click()  # add number btn
        sip_number = driver.find_element_by_xpath("/html/body/div/div/form/div/div/div/input["
                                                  "@id='appbundle_sipnumber_sipNumber']").get_attribute("value")
        password = create_pass()
        flat_title = str(starting_flat) + "flat"
        driver.find_element_by_id("appbundle_sipnumber_password").send_keys(password)
        driver.find_element_by_id("appbundle_sipnumber_name").send_keys(flat_title)  # input name
        driver.find_element_by_xpath("/html/body/div/div/form/div/div/a[@class='btn btn-primary btn-block']").click()
        # To list btn for test
        #driver.find_element_by_xpath(
        #                        "/html/body/div/div/form/div/div/input[@class='btn btn-success btn-block']").click()
        # Create btn for use
        return str(sip_number) + ":" + str(password) + ":" + str(flat_title)
    except NoSuchElementException:
        clear_console()
        print(f"{cant_find_element + RESET_ALL}")
