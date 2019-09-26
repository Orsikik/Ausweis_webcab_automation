from base_page import BasePage
from base_element import BaseElement
from selenium.webdriver.common.by import By
import os


class MainPage(BasePage):
    url = 'https://my.ausweis.io/ru/users/~update/'
    image_path = os.path.abspath('//home/ors/Pictures/download.jpeg')

    def photo_uploader(self):
        return BaseElement(self.driver, by=By.CSS_SELECTOR, value="input[type='file']")

    def name_field(self):
        return BaseElement(self.driver, by=By.ID, value="id_name")

    def phone_field(self):
        return BaseElement(self.driver, by=By.ID, value='id_phone')

    def submit_button(self):
        return BaseElement(self.driver, by=By.CSS_SELECTOR, value="button[type='submit']")

    def change_password_button(self):
        return BaseElement(self.driver, by=By.LINK_TEXT, value="Сменить пароль")



