# Initial imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from time import sleep

# Declaring the path and user agent along with a tab counter
PATH = "venv/chromedriver"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/" \
             "537.36 (KHTML, like Gecko) Chrome/" \
             "87.0.4280.88 Safari/537.36"
tab = 0

print("Welcome to Kahoot Flooder by xTobyPlayZ - Copyright (c) 2021")

# Getting the required user input
pin = int(input("Game Pin: "))
bot_name = input("Bot Name: ")
bot_amount = int(input("Bot Amount: "))

print(f"Sending {bot_amount} bots...")

# Declaring the options
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f"user-agent={USER_AGENT}")
options.add_argument("--window-size=1920,1080")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-running-insecure-content")
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=PATH, options=options)

# Main loop that runs the amount of times the user specifies
for i in range(bot_amount):
    if tab != 0:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[tab])

    # Navigating to Kahoot! (headless), then joining the game using
    # the provided pin and name the amount of times specified
    driver.get("https://kahoot.it")

    # Sending the bots
    pin_entry = driver.find_element_by_id("game-input")
    pin_entry.send_keys(pin)
    pin_entry.send_keys(Keys.RETURN)
    try:
        WebDriverWait(driver, 1).until(
            ec.presence_of_element_located(
                (By.ID, "nickname")))
        bot_name_entry = driver.find_element_by_id("nickname")
        bot_name_entry.send_keys(bot_name + str(i + 1))
        bot_name_entry.send_keys(Keys.RETURN)
    except TimeoutException:
        print("Pausing...")
        sleep(6)
        print("Continuing...")
    driver.delete_all_cookies()
    tab += 1

# Once the bots have been delivered, let the user wait until they want to
# delete them.
print("Bots have been delivered")
end = ""
while end == "":
    end = input("Type done to delete bots: ")
    if end == "done":
        driver.quit()
        print("Bots have been deleted (may take a moment to update on screen)")
    else:
        end = ""
print("Thank you for using Kahoot Flooder!")
