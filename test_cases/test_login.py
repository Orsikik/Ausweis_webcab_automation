
from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage

from browser_setting_up import browser


login_page_instance = LoginPage(browser)
login_page_instance.go()
login_page_instance.email_field().send_keys('i.orsyk@ausweis.io')

def test_success_login():
    pass

