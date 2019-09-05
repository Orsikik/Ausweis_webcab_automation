
from selenium import webdriver
from Base_page import BasePage
from Base_element import BaseElement
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


class LoginPage(BasePage):
    url = 'https://my.ausweis.io/ru/accounts/login/'

    def email_field(self):
        return BaseElement(self.driver, by=By.ID, value='id_login')

    def password_field(self):
        return BaseElement(self.driver, by=By.ID, value="id_password")

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


