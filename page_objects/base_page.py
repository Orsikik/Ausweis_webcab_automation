
from base_element import BaseElement


class BasePage:

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    @property
    def element(self, by, value):
        return BaseElement(
            driver=self.driver,
            by=by,
            value=value)






