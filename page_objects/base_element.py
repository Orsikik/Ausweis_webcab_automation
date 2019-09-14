
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseElement(object):

    def __init__(self, driver, value, by):
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)
        self.web_element = None
        self.find()

    def find(self):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    @property
    def click(self):
        element = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def send_keys(self, keys):
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator=self.locator))
        element.send_keys(keys)
        return None

    @property
    def text(self):
        text = self.web_element.text
        return text
