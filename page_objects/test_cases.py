from browser_setting_up import browser
from pytest import mark
from selenium.webdriver.common.keys import Keys
from pages import login_page, main_page, side_bar, profile_page, \
                  change_password_page, share_key_page, notification_page, activity_page, lock_page, edit_key_page
from time import sleep, gmtime, strftime, time
time_now = strftime("%Y-%m-%d %H:%M", gmtime(time() + 10800))
time_plus_5_minutes = strftime("%Y-%m-%d %H:%M", gmtime(time() + 10800))



# @mark.login
# def test_login_with_invalid_email_data():
#     login_page.go()
#     login_page.email_field.send_keys('')
#     login_page.password_field.send_keys('pepsicola')
#     login_page.enter_button.click
#     assert browser.current_url == 'https://my.ausweis.io/ru/accounts/login/'
#
#
# @mark.login
# def test_login_with_invalid_password():
#     login_page.go()
#     login_page.email_field.send_keys('i.orsyk@ausweis.io')
#     login_page.password_field.send_keys('pepsicolaa')
#     login_page.enter_button.click
#     assert browser.current_url == 'https://my.ausweis.io/ru/accounts/login/'
#
# @mark.smoke
# @mark.login
# def test_login_success():
#     login_page.go()
#     login_page.email_field.send_keys('i.orsyk@ausweis.io')
#     login_page.password_field.send_keys('pepsicola')
#     login_page.enter_button.click
#     assert browser.current_url == "https://my.ausweis.io/ru/keys/my/"

# @mark.smoke
# @mark.edit_profile
# class EditProfileTests:
#
#     def test_go_to_edit_profile(self):
#         login_page.go()
#         login_page.email_field.send_keys('i.orsyk@ausweis.io')
#         login_page.password_field.send_keys('pepsicola')
#         login_page.enter_button.click
#         side_bar.profile_options_list_opener.click
#         side_bar.edit_profile_button.click
#         assert browser.current_url == "https://my.ausweis.io/ru/users/~update/"
#
#     def change_image(self):
#         pass
#         #TODO find a way how to check images
#
#     def test_change_name_valid_data(self):
#         profile_page.name_field.clear
#         profile_page.name_field.send_keys("Pytester")
#         profile_page.submit_button.click
#         assert profile_page.name_field.get_attribute("value") == "Pytester"
#
#     def test_change_phone_valid_data(self):
#         profile_page.phone_field.clear
#         profile_page.phone_field.send_keys("+380951110011")
#         profile_page.submit_button.click
#         assert profile_page.phone_field.get_attribute("value") == "+380 95 111 0011"
#
#     def test_go_to_change_password_page(self):
#         profile_page.change_password_button.click
#         assert browser.current_url == "https://my.ausweis.io/ru/accounts/password/change/"
#
#     def test_change_password(self):
#         change_password_page.current_password_field.send_keys('pepsicola')
#         change_password_page.new_password_field.send_keys("PepsiCola1")
#         change_password_page.new_password_again_field.send_keys("PepsiCola1")
#         change_password_page.change_password_button.click
#         time.sleep(7)
#         main_page.dropdown_to_exit_button.click
#         main_page.exit_button.click
#         login_page.email_field.send_keys("i.orsyk@ausweis.io")
#         login_page.password_field.send_keys("PepsiCola1")
#         login_page.enter_button.click
#         assert browser.current_url == "https://my.ausweis.io/ru/keys/my/"
#
#     def test_tear_down(self):
#         side_bar.profile_options_list_opener.click
#         side_bar.edit_profile_button.click
#         profile_page.name_field.clear
#         profile_page.name_field.send_keys("Orsyk Igor")
#         profile_page.phone_field.clear
#         profile_page.phone_field.send_keys("+380951110011")
#         profile_page.submit_button.click
#         profile_page.change_password_button.click
#         change_password_page.current_password_field.send_keys('PepsiCola1')
#         change_password_page.new_password_field.send_keys("pepsicola")
#         change_password_page.new_password_again_field.send_keys("pepsicola")
#         change_password_page.change_password_button.click
#         main_page.dropdown_to_exit_button.click
#         main_page.exit_button.click

# @mark.lock_opening
# class LockFunctionsAndActivityTests:
#
#     def test_lock_opening(self, loging_in):
#         main_page.lock_tap_to_unlock_button.click
#         main_page.lock_ok_button_after_openning.click
#         assert browser.find_elements_by_class_name("sweet-confirm")[0].is_displayed() == False
#
#     def test_notification_appears_after_lock_opening(self):
#         side_bar.activity_button.click
#         print(activity_page.lock_last_notification().text)
#
#     def test_notification_appears_after_lock_opening(self):
#         side_bar.activity_button.click
#         time.sleep(0.5)
#         by_hum = activity_page.lock_last_notification.text
#         assert by_hum[23:28] == 'by me'


@mark.key_sharing
class KeySharingTests():

    # def test_unlimited_sharing(self, loging_in):
    #     side_bar.share_a_key_button.click
    #     share_key_page.email_field.send_keys("i.orsyk+12@ausweis.io")
    #     share_key_page.lock_list.click
    #     share_key_page.lock_list.send_keys(Keys.ARROW_DOWN)
    #     share_key_page.lock_list.send_keys(Keys.ARROW_DOWN)
    #     share_key_page.lock_list.send_keys(Keys.ARROW_DOWN)
    #     share_key_page.lock_list.send_keys(Keys.ENTER)
    #     share_key_page.driver.find_elements_by_xpath("//*[@id='div_id_limited']/div/div[1]/label/span/span[2]")[0].click()
    #     share_key_page.share_key_button.click
    #     assert lock_page.last_user.text == 'Auto Tester'
    #
    # def test_delete_shared_key(self):
    #     lock_page.delete_last_shared_key.click
    #     assert lock_page.last_user.text != 'Auto Tester'
    #
    # def test_share_limited_one_use_key(self, choose_lock, delete_lock):
    #     share_key_page.driver.find_elements_by_xpath("//*[@id='div_id_limited']/div/div[1]/label/span/span[2]")[0].click()
    #     share_key_page.driver.find_elements_by_xpath("//*[@id='div_id_one_time']/label/span/span[2]")[0].click()
    #     sleep(1)
    #     share_key_page.share_key_button.click
    #     lock_page.edit_shared_key.click
    #     assert edit_key_page.one_opening_checkbox.get_attribute('class') == "checkbox checked"
    #
    # def test_share_time_limits_key(self, choose_lock, delete_lock):
    #     share_key_page.driver.find_elements_by_xpath("//*[@id='div_id_limited']/div/div[2]/label/span/span[2]")[0].click()
    #     share_key_page.range_sharing_from_field.send_keys(time_now)
    #     share_key_page.range_sharing_to_field.send_keys(time_plus_5_minutes)
    #     share_key_page.share_key_button.click
    #     lock_page.edit_shared_key.click
    #     assert edit_key_page.limited_opening_checkbox.get_attribute('class') == "radio checked"

    def test_share_schedule_key(self, loging_in, choose_lock):
        share_key_page.driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/form/"
                                                           "div[7]/div/label/span/span[2]")[0].click()
        share_key_page.schedule_days_check_box(3).click
        share_key_page.schedule_start_field.click
        share_key_page.set_start_h(5).click
        share_key_page.ok_button_on_schedule_start_popup.click
        share_key_page.set_start_m(10).click
        share_key_page.ok_button_on_schedule_start_popup.click
        share_key_page.schedule_end_field.click
        share_key_page.set_start_h(6).click
        share_key_page.ok_button_on_schedule_end_popup.click
        # share_key_page.set_end_m(15).click
        a = share_key_page.driver.find_elements_by_xpath("//div[@id='dtp_FsRHG']/div[ @class ='dtp-content']/div[@class='dtp-date-view']/div[3]/div[2]/div[2]/*/*/*[@id='m-28']")[0].click()
        # for i in a:
        #     i[0].click()
        share_key_page.ok_button_on_schedule_end_popup.click

        # share_key_page.schedule_fields(12, 15, 'start')
        # share_key_page.schedule_fields(12, 30, 'end')

