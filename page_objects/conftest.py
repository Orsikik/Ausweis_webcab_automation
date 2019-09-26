from pytest import fixture
from selenium import webdriver
# from config_example import Config
from selenium.webdriver.chrome.options import Options
from browser_setting_up import browser
from pages import login_page, side_bar, share_key_page, main_page, lock_page
from selenium.webdriver.common.keys import Keys

@fixture(scope="class")
def loging_in():
    login_page.go()
    login_page.email_field.send_keys("i.orsyk@ausweis.io")
    login_page.password_field.send_keys("pepsicola")
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
def delete_lock():
    yield
    side_bar.my_locks_button.click
    main_page.lock_drop_down_parameters_button.click
    main_page.lock_settings_button.click
    lock_page.sent_keys.click
    lock_page.delete_last_shared_key.click

@fixture(scope='session')  # or 'function' if I want to open a new browser window in each function
def chrome():
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    option.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 2
    })

    browser = webdriver.Chrome(chrome_options=option,
                               executable_path=r'/home/ors/Dev/Selenium/drivers/chromedriver.exe')
    return browser


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Environment to run tests")


@fixture(scope="session")
def env(request):
    return request.config.getoption("--env")


# @fixture(scope="session")
# def app_config(env):
#     conf = Config(env)
#     return conf


@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Edge])
def browser(request):
    driver = request.param
    drv = driver()
    yield drv
    drv.quit()