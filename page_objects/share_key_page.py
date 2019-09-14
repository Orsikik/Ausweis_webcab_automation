from base_page import BasePage
from base_element import BaseElement
from selenium.webdriver.common.by import By


class ShareKeyPage(BasePage):
    url = 'https://my.ausweis.io/ru/keys/share/'

    def email_field(self):
        return BaseElement(self.driver, by=By.XPATH, value="//tbody/tr[1]/td")

    def lock_list(self):
        return BaseElement(self.driver, by=By.ID, value="id_lock")

    def unlimited_sharing_check_box(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='div_id_limited']/div/div[1]/label/span/span[2]")
        return web_element[0]

    def limited_sharing_check_box(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='div_id_limited']/div/div[2]/label/span/span[2]")
        return web_element[0]

    def one_opening_sharing_check_box(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='div_id_one_time']/label/span/span[2]")
        return web_element[0]

    def range_sharing_from_field(self):
        web_element = BaseElement(self.driver, by=By.ID,
                                  value="id_range_0")
        return web_element[0]

    def range_sharing_to_field(self):
        web_element = BaseElement(self.driver, by=By.ID,
                                  value="id_range_1")
        return web_element[0]

    def give_access_to_lock_activity_check_box(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='div_id_activity']/label/span/span[2]")
        return web_element[0]

    def schedule_check_box(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='id_with_schedule']")
        return web_element[0]

    def schedule_days_check_box(self, day_number):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value=f"//*[@id='div_id_schedule-0-days']/div/div[{day_number}]/label/span")
        return web_element[0]

    def schedule_monday_check_box(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='div_id_schedule-0-days']/div/div[1]/label/span")
        return web_element[0]

    def schedule_tuesday_check_box(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='div_id_schedule-0-days']/div/div[2]/label/span/span[2]")
        return web_element[0]

    def schedule_wednesday_check_box(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='div_id_schedule-0-days']/div/div[3]/label/span/span[2]")
        return web_element[0]

    def schedule_thursday_check_box(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='div_id_schedule-0-days']/div/div[4]/label/span/span[2]")
        return web_element[0]

    def schedule_friday_check_box(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='div_id_schedule-0-days']/div/div[5]/label/span/span[2]")
        return web_element[0]

    def schedule_saturday_check_box(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='div_id_schedule-0-days']/div/div[6]/label/span/span[2]")
        return web_element[0]

    def schedule_sunday_check_box(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="//*[@id='div_id_schedule-0-days']/div/div[7]/label/span/span[2]")
        return web_element[0]

    def schedule_fields(self, hour, minute, field='start'):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value=f"//*[@id='id_schedule-0-{field}']")
        web_element[0].click()

        def set_hour(hour):
            hours_list = []
            for indicator in range(23):
                hours_list.append(self.driver.find_elements_by_xpath(f"//*[@id='th-{indicator}']")[0])
            hours_list[hour].click()
            self.driver.find_elements_by_class_name("dtp-btn-ok")[0].click()

        def set_minute(minute):
            minute_for_list = None
            if minute == 0:
                minute_for_list = 0
            else:
                minute_for_list = minute / 5
            minutes_list = []
            for indicator in range(1, 13):
                minutes_list.append(self.driver.find_elements_by_xpath(f"//div[@class='dtp']//div[@class='dtp-content']"
                                                                       f"//div[@class='dtp-date-view']"f""
                                                                       f"//div[@class='dtp-picker']"
                                                                       f"//div[@class='dtp-picker-datetime']"f""
                                                                       f"//div[@id]//*[name()='svg']"
                                                                       f"//*[name()='g']"
                                                                       f"//*[name()='text'][{indicator}]"))
            minutes_list[int(minute_for_list)][0].click()
            self.driver.find_elements_by_class_name("dtp-btn-ok")[0].click()

        set_hour(hour)
        set_minute(minute)

    def share_key_button(self):
        web_element = BaseElement(self.driver, by=By.XPATH,
                                  value="/html/body/div[1]/div[2]/div/div/div/div/div/div/form/div[10]/div/button")
        return web_element[0]
