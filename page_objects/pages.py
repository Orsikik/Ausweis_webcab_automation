import os
from base_page import BasePage
from base_element import BaseElement
from selenium.webdriver.common.by import By
from browser_setting_up import browser
from time import sleep


class LoginPage(BasePage):
    url = 'https://my.ausweis.io/ru/accounts/login/'

    @property
    def email_field(self):
        return BaseElement(self.driver, by=By.ID, value='id_login')

    @property
    def password_field(self):
        return BaseElement(self.driver, by=By.ID, value="id_password")

    @property
    def enter_button(self):
        return BaseElement(self.driver,
                           by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div/div/div/div[3]/form/div[3]/button')

    def forget_password_button(self):
        return BaseElement(self.driver, by=By.LINK_TEXT, value='Забыли пароль?')

    def sign_up_button(self):
        return BaseElement(self.driver, by=By.LINK_TEXT, value='Sign Up')

    def facebook_button(self):
        return BaseElement(self.driver, by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div/div/div/div[2]/a[1]/i')

    def google_button(self):
        return BaseElement(self.driver, by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div/div/div/div[2]/a[2]/i')


class SideBar(BasePage):

    @property
    def user_name_text(self):
        return BaseElement(self.driver, by=By.XPATH, value='/html/body/div[1]/div[1]/div[3]/div/div[2]/a/text()')

    @property
    def profile_options_list_opener(self):
        return BaseElement(self.driver, by=By.XPATH, value="//a[@class='collapsed']")

    @property
    def edit_profile_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//a[text()='Edit Profile']")

    @property
    def my_locks_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[1]/a")

    @property
    def share_a_key_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[2]/a")

    @property
    def notifications_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[3]/a")

    @property
    def activity_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[4]/a")

    @property
    def balance_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[5]/a")

    @property
    def plans_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[6]/a")

    @property
    def groups_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[2]/a")


class MainPage(BasePage):
    url = 'https://my.ausweis.io/ru/keys/my/'

    @property
    def lock_tap_to_unlock_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//h5[text()='auto t']/../../div[3]/div[2]/a")

    @property
    def lock_ok_button_after_openning(self):
        return BaseElement(self.driver, by=By.CLASS_NAME, value="sweet-confirm")

    @property
    def lock_drop_down_parameters_button(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="//h5[text()='auto t']/../div/div/a/i")

    @property
    def lock_share_a_key_button(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="//h5[text()='auto t']/../../div[1]/div/div/ul/li[1]")[0]

    @property
    def lock_settings_button(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="//h5[text()='auto t']/../../div[1]/div/div/ul/li[2]")

    @property
    def owner_locks_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='nav-container nav-keys']/ul/li[1]/a")

    def shared_keys_list_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='nav-container nav-keys']/ul/li[2]/a")

    @property
    def dropdown_to_exit_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//a[@class='dropdown-toggle']/i")

    @property
    def exit_button(self):
        return BaseElement(self.driver, by=By.ID, value="logout")

class ProfilePage(BasePage):
    url = 'https://my.ausweis.io/ru/users/~update/'
    image_path = os.path.abspath('//home/ors/Pictures/download.jpeg')

    def photo_uploader(self):
        return BaseElement(self.driver, by=By.CSS_SELECTOR, value="input[type='file']")

    @property
    def name_field(self):
        return BaseElement(self.driver, by=By.ID, value="id_name")

    @property
    def phone_field(self):
        return BaseElement(self.driver, by=By.ID, value='id_phone')

    @property
    def submit_button(self):
        return BaseElement(self.driver, by=By.CSS_SELECTOR, value="button[type='submit']")

    @property
    def change_password_button(self):
        return BaseElement(self.driver, by=By.LINK_TEXT, value="Сменить пароль")


class ChangePasswordPage(BasePage):
    url = 'https://my.ausweis.io/ru/users/~update/'

    @property
    def current_password_field(self):
        return BaseElement(self.driver, by=By.ID, value="id_oldpassword")

    @property
    def new_password_field(self):
        return BaseElement(self.driver, by=By.ID, value="id_password1")

    @property
    def new_password_again_field(self):
        return BaseElement(self.driver, by=By.ID, value="id_password2")

    @property
    def change_password_button(self):
        return BaseElement(self.driver, by=By.NAME, value="action")


class ShareKeyPage(BasePage):
    url = 'https://my.ausweis.io/ru/keys/share/'

    @property
    def email_field(self):
        return BaseElement(self.driver, by=By.XPATH, value="//*[@id='id_to_user']")

    @property
    def lock_list(self):
        return BaseElement(self.driver, by=By.ID, value="id_lock")

    @property
    def unlimited_sharing_check_box(self):
        element = self.driver.find_elements_by_xpath("//*[@id='div_id_limited']/div/div[1]/label/span/span[2]")[0]
        return element

    @property
    def limited_sharing_check_box(self):
        return self.driver.find_elements_by_xpath("//*[@id='div_id_limited']/div/div[2]/label/span/span[2]")[0]

    @property
    def range_sharing_from_field(self):
        web_element = BaseElement(self.driver, by=By.ID,
                                  value="id_range_0")
        return web_element

    @property
    def range_sharing_to_field(self):
        web_element = BaseElement(self.driver, by=By.ID,
                                  value="id_range_1")
        return web_element

    @property
    def one_opening_sharing_check_box(self):
        return BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='div_id_one_time']/label/span/span[2]")

    @property
    def give_access_to_lock_activity_check_box(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='div_id_activity']/label/span/span[2]")
        return web_element[0]

    @property
    def schedule_check_box(self):
        return BaseElement(self.driver, by=By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/form/"
                                                           "div[7]/div/label/span/span[2]")

    def schedule_days_check_box(self, day_number):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value=f"//*[@id='div_id_schedule-0-days']/div/div[{day_number}]/label/span")
        return web_element

    @property
    def schedule_start_field(self):
        return BaseElement(self.driver, by=By.XPATH,
                                  value=f"//*[@id='id_schedule-0-start']")

    def set_start_h(self, hour):
        return BaseElement(self.driver, by=By.XPATH,
                                  value=f"//*[@id='th-{hour}']")

    def set_start_m(self, minute):
        return BaseElement(self.driver, by=By.XPATH,
                           value=f"//*[@id='tm-{minute}']")

    @property
    def ok_button_on_schedule_start_popup(self):
        return BaseElement(self.driver, by=By.CLASS_NAME,
                           value="dtp-btn-ok")

    @property
    def schedule_end_field(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value=f"//*[@id='id_schedule-0-end']")

    def set_end_h(self, hour):
        return BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='th-5']")

    def set_end_m(self, minute):
        return BaseElement(self.driver, by=By.XPATH,
                           value=f"//div[@id='dtp_FsRHG']/div[ @class ='dtp-content']/div[@class='dtp-date-view']/div[3]/div[2]/div[2]/*/*/*[@id='tm-{minute}']")

    @property
    def ok_button_on_schedule_end_popup(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="/html/body/div[3]/div/div[2]/button[4]")


    def set_hour(self, hour):
        hours_list = []
        for indicator in range(23):
            hours_list.append(self.driver.find_elements_by_xpath(f"//*[@id='th-{indicator}']")[0])
        hours_list[hour].click()
        self.driver.find_elements_by_class_name("dtp-btn-ok")[0].click()

    def set_minute(self, minute):
        minute_for_list = None
        if minute == 0:
            minute_for_list = 0
        else:
            minute_for_list = minute / 5
        minutes_list = []
        for indicator in range(1, 13):
            minutes_list.append(self.driver.find_elements_by_xpath(f"//div[@class='dtp']//div[@class='dtp-content']"
                                                                   f"//div[@class='dtp-date-view']"f""
                                                                   f"//div[@class='dtp-picker']"
                                                                   f"//div[@class='dtp-picker-datetime']"f""
                                                                   f"//div[@id]//*[name()='svg']"
                                                                   f"//*[name()='g']"
                                                                   f"//*[name()='text'][{indicator}]"))
        minutes_list[int(minute_for_list)][0].click()
        self.driver.find_elements_by_class_name("dtp-btn-ok")[0].click()


    def schedule_fields(self, hour, minute, field='start'):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value=f"//*[@id='id_schedule-0-{field}']")
        web_element.click
        sleep(1)
        self.set_hour(hour)
        sleep(1)
        self.set_minute(minute)

    @property
    def share_key_button(self):
        return BaseElement(self.driver, by=By.XPATH,
                                  value="/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[10]/div/button")


class ActivityPage(BasePage):
    url = 'https://my.ausweis.io/ru/notifications/list/'

    @property
    def lock_last_notification(self):
        return BaseElement(self.driver, by=By.XPATH, value="//tbody/tr[1]")


class NotificationPage(BasePage):
    url = 'https://my.ausweis.io/ru/notifications/list/'

    @property
    def lock_last_notification(self):
        return BaseElement(self.driver, by=By.XPATH, value="//tbody/tr[1]/td")


class LockPage(BasePage):

    def lock_details(self):
        pass

    @property
    def sent_keys(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="/html/body/div[1]/div[2]/div[1]/div/div/div[1]/ul/li[2]/a")

    @property
    def last_user(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="//*[@id='bootstrap-table-keys']/tbody/tr[1]/td[3]")

    @property
    def edit_shared_key(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="//*[@id='bootstrap-table-keys']/tbody/tr/td[5]/a[1]/i")

    @property
    def delete_last_shared_key(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="//*[@id='bootstrap-table-keys']/tbody/tr[1]/td[5]/a[2]/i")

    def activity(self):
        pass

    def activity_last_action(self):
        pass

    def admins(self):
        pass

    def admins_admin(self):
        pass


class EditSharedKeyPage(BasePage):

    @property
    def one_opening_checkbox(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="/html/body/div[1]/div[2]/div/div/div/div[1]/div/div/form/div[3]/div")

    @property
    def limited_opening_checkbox(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="//*[@id='div_id_limited']/div/div[2]")

    @property
    def schedule_start_field(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="//*[@id='id_schedule-0-start']")

    @property
    def schedule_end_field(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="//*[@id='id_schedule-0-end']")



login_page = LoginPage(browser)
main_page = MainPage(browser)
side_bar = SideBar(browser)
profile_page = ProfilePage(browser)
change_password_page = ChangePasswordPage(browser)
share_key_page = ShareKeyPage(browser)
notification_page = NotificationPage(browser)
activity_page = ActivityPage(browser)
lock_page = LockPage(browser)
edit_key_page = EditSharedKeyPage(browser)




