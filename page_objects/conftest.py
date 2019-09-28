from pytest import fixture
from selenium import webdriver
# from config_example import Config
from selenium.webdriver.chrome.options import Options
from browser_setting_up import browser
from time import sleep
from pages import login_page, side_bar, share_key_page, main_page, lock_page, profile_page, change_password_page
from selenium.webdriver.common.keys import Keys
from time_variables import time_now, time_plus_5_minutes, current_hour, current_round_minute


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests")


@fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


@fixture(scope="function")
def logging_in_main():
    login_page.go()
    login_page.email_field.send_keys("i.orsyk@ausweis.io")
    login_page.password_field.send_keys("pepsicola")
    login_page.enter_button.click


@fixture(scope="function")
def logging_in_second():
    login_page.go()
    login_page.email_field.send_keys("i.orsyk+12@ausweis.io")
    login_page.password_field.send_keys("PepsiCola1%")
    login_page.enter_button.click


@fixture(scope='function')
def choose_lock():
    side_bar.share_a_key_button.click
    share_key_page.email_field.send_keys("i.orsyk+12@ausweis.io")
    share_key_page.lock_list.click
    share_key_page.lock_list.send_keys(Keys.ARROW_DOWN)
    share_key_page.lock_list.send_keys(Keys.ARROW_DOWN)
    share_key_page.lock_list.send_keys(Keys.ARROW_DOWN)
    share_key_page.lock_list.send_keys(Keys.ENTER)


@fixture(scope='function')
def share_unlimited_key():
    share_key_page.driver.find_elements_by_xpath("//*[@id='div_id_limited']/div/div[1]/label/span/span[2]")[0].click()
    share_key_page.share_key_button.click


@fixture(scope='function')
def share_one_use_key():
    share_key_page.driver.find_elements_by_xpath("//*[@id='div_id_limited']/div/div[1]/label/span/span[2]")[0].click()
    share_key_page.driver.find_elements_by_xpath("//*[@id='div_id_one_time']/label/span/span[2]")[0].click()
    sleep(1)
    share_key_page.share_key_button.click
    lock_page.edit_shared_key.click

@fixture(scope='function')
def share_time_limit_key():
    share_key_page.driver.find_elements_by_xpath("//*[@id='div_id_limited']/div/div[2]/label/span/span[2]")[0].click()
    share_key_page.range_sharing_from_field.send_keys(time_now)
    share_key_page.range_sharing_to_field.send_keys(time_plus_5_minutes)
    share_key_page.share_key_button.click
    lock_page.edit_shared_key.click


@fixture(scope='function')
def share_schedule_key():
    share_key_page.driver.find_elements_by_xpath("//*[@id='div_id_limited']/div/div[1]/label/span/span[2]")[0]. \
        click()
    share_key_page.driver.find_elements_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div/div/form/"
                                                 "div[7]/div/label/span/span[2]")[0].click()
    share_key_page.schedule_days_check_box(3).click
    share_key_page.schedule_start_field.click
    share_key_page.set_start_h(current_hour).click
    share_key_page.ok_button_on_schedule_start_popup.click
    sleep(1)
    share_key_page.set_start_m(current_round_minute).click
    share_key_page.ok_button_on_schedule_start_popup.click
    share_key_page.schedule_end_field.click
    share_key_page.set_start_h(int(current_hour) + 1).click
    share_key_page.ok_button_on_schedule_end_popup.click
    a = share_key_page.driver.find_elements_by_xpath("//div[@id='dtp_FsRHG']/div[ @class ='dtp-content']/"
                                                     "div[@class='dtp-date-view']/div[3]/div[2]/div[2]/*/*/*[@id='m-28']")
    for i in a:
        i[0].click()
    share_key_page.ok_button_on_schedule_end_popup.click
    share_key_page.share_key_button.click
    lock_page.edit_shared_key.click


@fixture(scope='function')
def delete_lock():
    yield
    side_bar.my_locks_button.click
    main_page.lock_drop_down_parameters_button.click
    main_page.lock_settings_button.click
    lock_page.sent_keys.click
    lock_page.delete_last_shared_key.click

@fixture(scope='function')
def tear_down_user_profile_settings():
    yield
    side_bar.profile_options_list_opener.click
    side_bar.edit_profile_button.click
    profile_page.name_field.clear
    profile_page.name_field.send_keys("Orsyk Igor")
    profile_page.phone_field.clear
    profile_page.phone_field.send_keys("+380952183724")
    profile_page.submit_button.click
    profile_page.change_password_button.click
    change_password_page.current_password_field.send_keys('PepsiCola1')
    change_password_page.new_password_field.send_keys("pepsicola")
    change_password_page.new_password_again_field.send_keys("pepsicola")
    change_password_page.change_password_button.click
    # TODO add pop up handler after the password change ( near the dropdown to exit)

@fixture(scope='function')
def exit_from_account():
    yield
    main_page.dropdown_to_exit_button.click
    main_page.exit_button.click





