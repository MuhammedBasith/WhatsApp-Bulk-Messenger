"""
WhatsApp Bulk Messaging - Number Extractor

Author: Basith
Contact: iambasith123@gmail.com

This script allows you to extract phone numbers from a WhatsApp group and store them in a text file.

Usage:
1. Open WhatsApp Web and sign in.
2. Pin the group whose participant numbers you want to extract.
3. Run this script to extract and store the numbers.

Requirements:
- Python 3.x
- Selenium library
- Chrome web browser
- ChromeDriver

"""


import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
# TODO: Replace the below value with an actual path to a new folder, follow this format 'C:\\Users\\Desktop\\userdir'
user_dir = 'Give your path over here'
options.add_argument(f"--user-data-dir={user_dir}")

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://web.whatsapp.com/')

input('Press Enter after scanning QR code and loading WhatsApp Web')

time.sleep(2)
group_element = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[4]/div/div[2]/div[1]/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]")
group_element.click()

time.sleep(5)
element = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[5]/div/header/div[2]/div[2]/span')

numbers_text = element.get_attribute("title")
numbers = [number.strip() for number in numbers_text.split(",")]
# print(numbers)

with open("numbers.txt", "w") as file:
    for number in numbers:
        if number != 'You':
            file.write(number + "\n")

driver.quit()
