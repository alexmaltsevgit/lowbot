from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from browser.GetAllElBy import GetAllElBy
from browser.GetElBy import GetElBy


class WrappedChrome(webdriver.Chrome):
    def __init__(self, click_sleep_time=0.5, field_fill_sleep_time=0.5, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.click_sleep_time = click_sleep_time
        self.field_fill_sleep_time = field_fill_sleep_time

    @property
    def get_el_by(self):
        get_el_by = GetElBy(self)
        return get_el_by

    @property
    def get_all_el_by(self):
        get_all_el_by = GetAllElBy(self)
        return get_all_el_by

    def click_on(self, element, sleep_after: int = None):
        sleep_after = self.click_sleep_time if sleep_after is None else self.click_sleep_time

        element = self._convert_to_web_element(element)
        element.click()
        sleep(sleep_after)

    def click_on_many(self, elements, sleep_after: int = None):
        sleep_after = self.click_sleep_time if sleep_after is None else self.click_sleep_time

        for element in elements:
            self.click_on(element, sleep_after)

    def click_on_repeatedly(self, element, times: int, sleep_after: int = None):
        sleep_after = self.click_sleep_time if sleep_after is None else self.click_sleep_time

        for i in times:
            self.click_on(element, sleep_after)

    def click_on_many_repeatedly(self, elements, times: int, sleep_after: int = None):
        sleep_after = self.click_sleep_time if sleep_after is None else self.click_sleep_time

        for i in times:
            self.click_on_many(elements, sleep_after)

    def fill_field(self, field, value: str, sleep_after: int = None):
        sleep_after = self.click_sleep_time if sleep_after is None else self.field_fill_sleep_time

        field: WebElement = self._convert_to_web_element(field)
        field.clear()
        field.send_keys(value)
        sleep(sleep_after)

    def fill_many_fields(self, fields_and_values: dict, sleep_after: int = None):
        sleep_after = self.click_sleep_time if sleep_after is None else self.field_fill_sleep_time

        for field, value in fields_and_values.items():
            self.fill_field(field, value, sleep_after)

    def wait_for(self, css_selector):
        el: WebElement = WebDriverWait(self, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, css_selector)
            )
        )

        return el

    def open_new_tab(self):
        self.execute_script("window.open();")
        self.switch_to.window(self.window_handles[1])

    def _convert_to_web_element(self, el) -> WebElement:
        if type(el) is str:
            el = self.find_element_by_css_selector(el)
        elif type(el) is WebElement:
            pass
        else:
            raise Exception('Wrong type. Expected str | WebElement')

        return el
