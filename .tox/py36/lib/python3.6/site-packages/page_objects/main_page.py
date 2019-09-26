from base_page import BasePage
from base_element import BaseElement
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    url = 'https://my.ausweis.io/ru/keys/my/'

    def lock_tap_to_unlock_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//h5[text()='TIW Main Entrance']/../../div[3]/div[2]/a")

    def lock_drop_down_parameters_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//h5[text()='TIW Main Entrance']/../../div/div/div/a")

    def lock_share_a_key_button(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="//h5[text()='TIW Main Entrance']/../../div[1]/div/div/ul/li[1]")

    def lock_settings_button(self):
        return BaseElement(self.driver, by=By.XPATH,
                           value="//h5[text()='TIW Main Entrance']/../../div[1]/div/div/ul/li[2]")

    def owner_locks_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='nav-container nav-keys']/ul/li[1]/a")

    def shared_keys_list_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='nav-container nav-keys']/ul/li[2]/a")




