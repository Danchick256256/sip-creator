from authorization import authorization
from tools.driver_init import init_driver
from tools.colors import RESET_ALL, FG, BOLD
from tools.text import done, cursor, quit_text, banner
from tools.clear_console import clear_console
from data_retrieval import data_retrieval


driver = init_driver()


def main():
    sip = open("sip.txt", "w")
    final_flat, starting_flat, number_of_repetitions = authorization(driver)
    clear_console()
    for _ in range(number_of_repetitions):
        sip.write(data_retrieval(starting_flat, driver) + "\n")
        clear_console()
        print(f"{banner}\n{FG.lightcyan}======================\n{RESET_ALL + BOLD + FG.lightcyan}Current number "
              f"{cursor + RESET_ALL}{starting_flat}{FG.lightcyan}\n======================{RESET_ALL}", sep='')
        starting_flat += 1
    clear_console()
    print(f"{done + RESET_ALL}")
    sip.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        clear_console()
        print(f"{quit_text}{RESET_ALL}")
    except TypeError:
        pass
    finally:
        driver.close()
        driver.quit()
