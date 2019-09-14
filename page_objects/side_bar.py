from base_page import BasePage
from base_element import BaseElement
from selenium.webdriver.common.by import By


class SideBar(BasePage):

    def user_name_text(self):
        return BaseElement(self.driver, by=By.XPATH, value='/html/body/div[1]/div[1]/div[3]/div/div[2]/a/text()')

    def profile_options_list_opener(self):
        return BaseElement(self.driver, by=By.XPATH, value="//a[@class='collapsed']")

    def edit_profile_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//a[text()='Edit Profile']")

    def my_locks_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[1]/a")

    def share_a_key_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[2]/a")

    def notifications_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[3]/a")

    def activity_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[4]/a")

    def balance_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[5]/a")

    def plans_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[6]/a")

    def groups_button(self):
        return BaseElement(self.driver, by=By.XPATH, value="//div[@class='sidebar-wrapper']/ul/li[2]/a")



