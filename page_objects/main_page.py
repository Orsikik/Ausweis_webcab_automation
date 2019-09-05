from base_page import BasePage
from base_element import BaseElement
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    url = 'https://my.ausweis.io/ru/keys/my/'

    def user_name_text(self):
        return BaseElement(self.driver, by=By.XPATH, value='/html/body/div[1]/div[1]/div[3]/div/div[2]/a/text()')

    def profile_options_list_opener(self):
        return BaseElement(self.driver, by=By.XPATH, value="//a[@class='collapsed']")

    def edit_profile_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//a[text()='Edit Profile']")

