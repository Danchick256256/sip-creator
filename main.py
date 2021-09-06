from authorization import authorization
from tools.driver_init import init_driver
from tools.colors import RESET_ALL, FG, BOLD
from tools.text import done, cursor, quit_text
from tools.clear_console import clear_console
from data_retrieval import data_retrieval


driver = init_driver()

def main():
    sip = open("sip.txt", "w")
    final_flat, starting_flat, number_of_repetitions = authorization(driver)
    clear_console()
    for i in range(number_of_repetitions):
        sip.write(data_retrieval(starting_flat, driver) + "\n")
        print(f"{BOLD + FG.lightcyan}Current number {cursor}{starting_flat}{RESET_ALL}", sep='')
        starting_flat += 1
    clear_console()
    print(f"{done + RESET_ALL}")
    sip.close()
    driver.quit()
    driver.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        clear_console()
        print(f"{quit_text}{RESET_ALL}")
    finally:
        driver.close()
        driver.quit()
