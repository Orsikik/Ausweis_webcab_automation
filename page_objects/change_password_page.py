from base_page import BasePage
from base_element import BaseElement
from selenium.webdriver.common.by import By


class ChangePasswordPage(BasePage):
    url = 'https://my.ausweis.io/ru/users/~update/'

    def current_password_field(self):
        return BaseElement(self.driver, by=By.ID, value="id_oldpassword")

    def new_password_field(self):
        return BaseElement(self.driver, by=By.ID, value="id_password1")

    def new_password_again_field(self):
        return BaseElement(self.driver, by=By.ID, value="id_password1")

    def change_password_button(self):
        return BaseElement(self.driver, by=By.NAME, value="action")


