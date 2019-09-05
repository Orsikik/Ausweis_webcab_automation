
from Page_Objects.Login_page import LoginPage
from Page_Objects.Main_page import MainPage

from browser_setting_up import browser


if __name__ == '__main__':

    login_page_instance = LoginPage(browser)

