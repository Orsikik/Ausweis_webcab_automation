from browser_setting_up import browser
from pytest import mark
from selenium.webdriver.common.keys import Keys
from pages import login_page, main_page, side_bar, profile_page, \
                  change_password_page, share_key_page, notification_page, activity_page, lock_page, edit_key_page
from time import sleep, gmtime, strftime, time
from time_variables import time_now, time_plus_5_minutes, current_hour, current_round_minute


# @mark.smoke
# class LoginTests():
#
#     def test_login_with_invalid_email_data(self):
#         login_page.go()
#         login_page.email_field.send_keys('')
#         login_page.password_field.send_keys('pepsicola')
#         login_page.enter_button.click
#         assert browser.current_url == 'https://my.ausweis.io/ru/accounts/login/'
#
#     def test_login_with_invalid_password(self):
#         login_page.go()
#         login_page.email_field.send_keys('i.orsyk@ausweis.io')
#         login_page.password_field.send_keys('pepsicolaa')
#         login_page.enter_button.click
#         assert browser.current_url == 'https://my.ausweis.io/ru/accounts/login/'
#
#     def test_login_success(self, logging_in_owner, exit_from_account_after):
#         assert browser.current_url == "https://my.ausweis.io/ru/keys/my/"



# @mark.smoke
# @mark.edit_profile
# class EditProfileTests:
#
#     def test_go_to_edit_profile(self, logging_in_owner):
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
#     def test_change_password(self, exit_from_account_after, tear_down_user_profile_settings):
#         profile_page.change_password_button.click
#         change_password_page.current_password_field.send_keys('pepsicola')
#         change_password_page.new_password_field.send_keys("PepsiCola1")
#         change_password_page.new_password_again_field.send_keys("PepsiCola1")
#         change_password_page.change_password_button.click
#         sleep(7)
#         main_page.dropdown_to_exit_button.click
#         main_page.exit_button.click
# #         login_page.email_field.send_keys("i.orsyk@ausweis.io")
#         login_page.password_field.send_keys("PepsiCola1")
#         login_page.enter_button.click
#         assert browser.current_url == "https://my.ausweis.io/ru/keys/my/"

#
# @mark.lock_opening
# class LockFunctionsAndActivityTests:
#
#     def test_lock_opening(self, logging_in_owner, open_my_key):
#         main_page.lock_ok_button_after_openning.click
#         assert browser.find_elements_by_class_name("sweet-confirm")[0].is_displayed() == False
#
#     def test_notification_appears_after_lock_opening(self, exit_from_account_after):
#         side_bar.activity_button.click
#         sleep(0.5)
#         by_hum = activity_page.lock_last_notification.text
#         assert by_hum[12:17] == 'by me'


@mark.key_sharing
class KeySharingTests():

    # def test_unlimited_sharing(self, logging_in_owner, choose_lock, share_unlimited_key):
    #     assert lock_page.last_user.text == 'Auto Tester'
    #
    # def test_delete_shared_key(self):
    #     side_bar.my_locks_button.click
    #     main_page.lock_drop_down_parameters_button.click
    #     main_page.lock_settings_button.click
    #     lock_page.sent_keys.click
    #     lock_page.delete_last_shared_key.click
    #     assert lock_page.last_user.text != 'Auto Tester'
    #
    # def test_share_limited_one_use_key(self, choose_lock, share_one_use_key, delete_key_from_owner):
    #     assert edit_key_page.one_opening_checkbox.get_attribute('class') == "checkbox checked"
    #
    # def test_share_time_limit_key(self, choose_lock, share_time_limit_key_current_and_plus_5, delete_key_from_owner):
    #     assert edit_key_page.limited_opening_checkbox.get_attribute('class') == "radio checked"
    #
    # def test_share_schedule_key(self, choose_lock, share_schedule_key, delete_key_from_owner):
    #     assert edit_key_page.schedule_start_field.get_attribute('value') == f'{current_hour}:{current_round_minute + 10}:00' #баг на 00 минутах и
    #
    # def test_check_sharing_unlimited_key_from_guest_account(self, choose_lock, share_unlimited_key,
    #                                                         exit_from_account_before, logging_in_quest):
    #     main_page.shared_keys_list_button.click
    #     main_page.lock_tap_to_unlock_button.click
    #     main_page.lock_ok_button_after_openning.click
    #     assert browser.find_elements_by_class_name("sweet-confirm")[0].is_displayed() == False
    #
    # def test_check_activity_after_guest_open_lock(self):
    #     side_bar.activity_button.click
    #     sleep(0.5)
    #     by_hum = activity_page.lock_last_notification.text
    #     assert by_hum[12:17] == 'by me'
    #
    # def test_delete_lock_from_guest(self, delete_key_from_guest_before, exit_from_account_after):
    #     assert main_page.key_popup_text.text == "Deleted!"
    #     main_page.success_delete_popup.click
    #
    # def test_open_shared_one_use_key_first_time(self, logging_in_owner, choose_lock, share_one_use_key,
    #                                                       exit_from_account_before, logging_in_quest, open_shared_key):
    #     assert main_page.lock_is_opening_popup.text == "Lock is opening"
    #     main_page.lock_ok_button_after_openning.click
    #
    #
    # def test_open_shared_one_use_key_second_time(self, open_shared_key, exit_from_account_after, delete_key_from_guest_after):
    #     assert main_page.key_popup_text.text == "Key is invalid"
    #     main_page.lock_ok_button_after_openning.click


    def test_open_shared_time_limit_key_before_permited_period(self, logging_in_owner, choose_lock, share_time_limit_key_plus_2_and_plus_4,
                                          exit_from_account_before, logging_in_quest, open_shared_key):
        assert main_page.key_popup_text.text == "Key is invalid"
        main_page.lock_ok_button_after_openning.click
        sleep(120)

    def test_open_shared_time_limit_key_durring_permited_period(self, open_shared_key):
        assert main_page.lock_is_opening_popup.text == "Lock is opening"
        main_page.lock_ok_button_after_openning.click
        sleep(150)

    def test_open_shared_time_limit_key_after_permited_period(self, open_shared_key, exit_from_account_after,
                                                      delete_key_from_guest_after):
        assert main_page.key_popup_text.text == "Key is invalid"
        main_page.lock_ok_button_after_openning.click

    def test_open_shared_schedule_key_before_permitted_period(self, logging_in_owner, choose_lock, share_schedule_key,
                                                              exit_from_account_before, logging_in_quest, open_shared_key):
        assert main_page.key_popup_text.text == "Key is out of schedule now"
        main_page.lock_ok_button_after_openning.click
        sleep(600)

    def test_open_shared_schedule_key_during_permitted_period(self, open_shared_key, delete_key_from_guest_after):
        assert main_page.lock_is_opening_popup.text == "Lock is opening"
        main_page.lock_ok_button_after_openning.click

