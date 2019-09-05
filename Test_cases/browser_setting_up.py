from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

browser = webdriver.Chrome(chrome_options=option, executable_path=r'/home/ors/Dev/Selenium/drivers/chromedriver.exe')
