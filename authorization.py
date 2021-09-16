from selenium.common.exceptions import NoSuchElementException

from tools.exceptions import OutOfNumbers, WrongPassOrEmail
from tools.clear_console import clear_console
from tools.colors import FG, BOLD, RESET_ALL
from tools.text import cursor, wrong_password, wrong_value, banner, cant_find_element, out_of_numbers


def authorization(driver):
    try:
        try:
            clear_console()
            starting_flat = int(input(f"{banner + FG.green + BOLD}Enter start number {cursor + RESET_ALL}"))
            final_flat = int(input(f"{FG.green + BOLD}Enter last number {cursor + RESET_ALL}"))
        except ValueError:
            clear_console()
            print(f"{wrong_value + RESET_ALL}")
            driver.quit()
        number_of_repetitions = final_flat - starting_flat + 1
        username = input(f"{BOLD + FG.green}Enter username {cursor + RESET_ALL}")
        password = input(f"{BOLD + FG.green}Enter password {cursor + RESET_ALL}")

        driver.get("https://sip.bas-ip.com/auth/login")

        driver.find_element_by_id("appbundle_login_email").send_keys(username)
        driver.find_element_by_id("appbundle_login_password").send_keys(password)
        driver.find_element_by_xpath(
            "/html/body/div/div/div/div/form/div/div/button[@class='btn btn-block btn-success']").click()  # Sing in btn
        try:
            driver.find_element_by_xpath("/html/body/div/nav/ul/li[2]/a").click()  # Virtual numbers
        except NoSuchElementException:
            raise WrongPassOrEmail
        try:
            driver.find_element_by_xpath("/html/body/div/div/div/a[@class='btn btn-lg btn-primary']")
        except NoSuchElementException:
            raise OutOfNumbers

        return final_flat, starting_flat, number_of_repetitions
    except WrongPassOrEmail:
        clear_console()
        print(f"{wrong_password + RESET_ALL}")
    except OutOfNumbers:
        clear_console()
        print(f"{out_of_numbers + RESET_ALL}")
