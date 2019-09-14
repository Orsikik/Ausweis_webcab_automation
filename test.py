# $x("//button[@id='ptm']") >>>> Xpath request
# $x("//b[text()='Product 1']/../../p")[0].inner.HTML >>>> complicated Xpath request
# $x("//*[name()='svg']//*[name()='g']//*[name()='text']")

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_all_elements_located
from selenium.webdriver.common.keys import Keys
import os
import time

#Set-up
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

browser = webdriver.Chrome(chrome_options=option,
                          executable_path=r'/home/ors/Dev/Selenium/drivers/chromedriver.exe')

alert = Alert(browser)



browser.get("https://my.ausweis.io/ru/accounts/login/")
email_field = browser.find_element_by_id("id_login")
password_field = browser.find_element_by_id("id_password")
enter_button = browser.find_element_by_css_selector("button[type='submit']")

email_field.send_keys('i.orsyk@ausweis.io')
password_field.send_keys('pepsicola')
enter_button.click()
share_key_button = browser.find_element_by_xpath("//div[@class='sidebar-wrapper']/ul/li[2]/a")
share_key_button.click()
time.sleep(1)
share_key_page_email_field = browser.find_element_by_id('id_to_user')
locks_list = browser.find_element_by_id('id_lock')
share_key_page_email_field.send_keys('test@email.com')
locks_list.click()
locks_list.send_keys(Keys.ARROW_DOWN)
locks_list.send_keys(Keys.ARROW_DOWN)
locks_list.send_keys(Keys.ARROW_DOWN)
locks_list.send_keys(Keys.ENTER)

unlimited = browser.find_elements_by_xpath("//*[@id='div_id_limited']/div/div[1]/label/span/span[2]")
unlimited[0].click()

schedule_checkbox = browser.find_elements_by_xpath("//*[@id='div_id_with_schedule']/label/span/span[2]")
schedule_checkbox[0].click()

time.sleep(1)
monday = browser.find_elements_by_xpath("//*[@id='div_id_schedule-0-days']/div/div[1]/label/span")
tuesday = browser.find_elements_by_xpath("//*[@id='div_id_schedule-0-days']/div/div[2]/label/span/span[2]")
wednesday = browser.find_elements_by_xpath("//*[@id='div_id_schedule-0-days']/div/div[3]/label/span/span[2]")
thursday = browser.find_elements_by_xpath("//*[@id='div_id_schedule-0-days']/div/div[4]/label/span/span[2]")
friday = browser.find_elements_by_xpath("//*[@id='div_id_schedule-0-days']/div/div[5]/label/span/span[2]")
saturday = browser.find_elements_by_xpath("//*[@id='div_id_schedule-0-days']/div/div[6]/label/span/span[2]")
sunday = browser.find_elements_by_xpath("//*[@id='div_id_schedule-0-days']/div/div[7]/label/span/span[2]")


monday[0].click()
tuesday[0].click()
wednesday[0].click()
thursday[0].click()
friday[0].click()
saturday[0].click()
sunday[0].click()

start = browser.find_elements_by_xpath("//*[@id='id_schedule-0-start']")
start[0].click()

time.sleep(1)


def set_time(hour, minute):
    def set_hour(hour):
        hours_list = []
        for indicator in range(23):
            hours_list.append(browser.find_elements_by_xpath(f"//*[@id='th-{indicator}']")[0])
        hours_list[hour].click()
        browser.find_elements_by_class_name('dtp-btn-ok')[0].click()


    def set_minute(minute):
        minute_for_list = None
        if minute == 0:
            minute_for_list = 0
        else:
            minute_for_list = minute / 5
        minutes_list = []
        for indicator in range(1, 13):
            minutes_list.append(browser.find_elements_by_xpath
                                (f"//div[@class='dtp']//div[@class='dtp-content']//div[@class='dtp-date-view']"
                                 f"//div[@class='dtp-picker']//div[@class='dtp-picker-datetime']"
                                 f"//div[@id]//*[name()='svg']//*[name()='g']//*[name()='text'][{indicator}]"))
        minutes_list[int(minute_for_list)][0].click()
        browser.find_elements_by_class_name("dtp-btn-ok")[0].click()

    set_hour(hour)
    set_minute(minute)


set_time(1, 45)




end = browser.find_elements_by_xpath("//*[@id='id_schedule-0-end']")
end[0].click()

time.sleep(1)


def set_time_end(hour, minute):
    def set_hour(hour):
        hours_list = []
        for indicator in range(23):
            hours_list.append(browser.find_elements_by_xpath(f"//*[@id='th-{indicator}']")[0])
        hours_list[hour].click()
        browser.find_elements_by_xpath("//div[@class='dtp-buttons']/button[text()='OK']")[1].click()


    def set_minute(minute):
        minute_for_list = None
        if minute == 0:
            minute_for_list = 0
        else:
            minute_for_list = minute / 5
        minutes_list = []
        for indicator in range(1, 13):
            minutes_list.append(browser.find_elements_by_xpath
                                (f"//div[@class='dtp']//div[@class='dtp-content']//div[@class='dtp-date-view']"
                                 f"//div[@class='dtp-picker']//div[@class='dtp-picker-datetime']"
                                 f"//div[@id]//*[name()='svg']//*[name()='g']//*[name()='text'][{indicator}]"))
        minutes_list[int(minute_for_list)][0].click()
        browser.find_elements_by_xpath("//div[@class='dtp-buttons']/button[text()='OK']")[1].click()

    set_hour(hour)
    set_minute(minute)


set_time_end(1, 50)

final_share_button = browser.find_elements_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[10]/div/button")
final_share_button[0].click()
# zero_hour = browser.find_elements_by_xpath("//*[@id='th-0']")[0]
# zero_hour.click()



# #Go to profile settings
# profile_options = browser.find_element_by_xpath("//a[@class='collapsed']")
# edit_profile = browser.find_element_by_xpath("//a[text()='Edit Profile']")
# profile_options.click()
# sleep(1)
# edit_profile.click()

# #Profile (change photo)
# imagepath = os.path.abspath('//home/ors/Pictures/download.jpeg')
# photo_uploader = browser.find_element_by_css_selector("input[type='file']")
# change_password = browser.find_element_by_link_text("Сменить пароль")
# change_password.click()

# wait.until(visibility_of_all_elements_located((By.LINK_TEXT, 'Edit Profile')))
# edit_profile.click()
#
#
# #Profile (change name)
#
# name_field = browser.find_element_by_id('id_name')
#
# # submit_button = browser.find_element_by_class_name("btn btn-fill btn-info")
#
# name_field.clear()
# name_field.send_keys('Igor Ausweis')
# name_field.send_keys(Keys.ENTER)

# phone_field = browser.find_element_by_id('id_phone')
# phone_field.clear()
# phone_field.send_keys(+380950000000)
# enter_button = browser.find_element_by_css_selector("button[type='submit']")
# enter_button.click()
# #phone_field = browser.find_element_by_id('id_phone')
# # name_field.send_keys(Keys.ENTER)


# #Side_bar
# profile_options = browser.find_element_by_xpath("//a[@class='collapsed']")
# edit_profile = browser.find_element_by_xpath("//a[text()='Edit Profile']")
# my_locks = browser.find_element_by_xpath("//div[@class='sidebar-wrapper']/ul/li[1]/a")
# shared_locks = browser.find_element_by_xpath("//div[@class='sidebar-wrapper']/ul/li[2]/a")
# notification_button = browser.find_element_by_xpath("//div[@class='sidebar-wrapper']/ul/li[3]/a")

# #Change password
# current_password = browser.find_element_by_id("id_oldpassword")
# current_password.send_keys('PepsiCola1')
# new_password = browser.find_element_by_id("id_password1")
# new_password.send_keys('pepsicola')
# new_password_again = browser.find_element_by_id("id_password2")
# new_password_again.send_keys("pepsicola")
# submit_password = browser.find_element_by_name("action")
# submit_password.click()


#TODO: How to do screens while testingо
#TODO: HOw to pass the error