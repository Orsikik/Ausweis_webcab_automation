from base_page import BasePage
from base_element import BaseElement
from selenium.webdriver.common.by import By


class LockActivityPage(BasePage):
    url = 'https://my.ausweis.io/ru/notifications/list/'

    def lock_last_notification(self):
        return BaseElement(self.driver, by=By.XPATH, value="//tbody/tr[1]")