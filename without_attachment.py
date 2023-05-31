"""
WhatsApp Bulk Messaging - Without Attachment

Author: Basith
Contact: iambasith123@gmail.com

This script allows you to send plain text bulk messages on WhatsApp.

Usage:
1. Prepare a message file with your custom message.
2. Create a numbers file with the phone numbers of the recipients.
3. Run this script to send plain text messages.

Requirements:
- Python 3.x
- Selenium library
- Chrome web browser
- ChromeDriver

"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
# TODO: Replace the below value with an actual path to a new folder, follow this format 'C:\\Users\\Desktop\\userdir'
user_dir = 'Give your path over here'
options.add_argument(f"--user-data-dir={user_dir}")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"


class Style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


f = open("message.txt", "r", encoding="utf8")
message = f.read()
f.close()

print(Style.YELLOW + '\nThis is your message-')
print(Style.GREEN + message)
print("\n" + Style.RESET)
message = quote(message)

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
    if line.strip() != "":
        numbers.append(line.strip())
f.close()
total_number = len(numbers)
print(Style.RED + 'We found ' + str(total_number) + ' numbers in the file' + Style.RESET)
delay = 30

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(
    Style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + Style.RESET)
for idx, number in enumerate(numbers):
    number = number.strip()
    if number == "":
        continue
    print(Style.YELLOW + '{}/{} => Sending message to {}.'.format((idx + 1), total_number, number) + Style.RESET)
    try:
        url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
        sent = False
        for i in range(3):
            if not sent:
                driver.get(url)
                try:
                    click_btn = WebDriverWait(driver, delay).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
                except Exception as e:
                    print(Style.RED + f"\nFailed to send message to: {number}, retry ({i + 1}/3)")
                    print("Make sure your phone and computer is connected to the internet.")
                    print("If there is an alert, please dismiss it." + Style.RESET)
                else:
                    sleep(1)
                    click_btn.click()
                    sent = True
                    sleep(3)
                    print(Style.GREEN + 'Message sent to: ' + number + Style.RESET)
    except Exception as e:
        print(Style.RED + 'Failed to send message to ' + number + str(e) + Style.RESET)

driver.close()
