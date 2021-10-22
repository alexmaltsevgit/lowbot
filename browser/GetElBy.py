from utils.decorators import decorate_all_methods, return_default_on_exception
from selenium.common.exceptions import NoSuchElementException


@decorate_all_methods(return_default_on_exception(None, NoSuchElementException))
class GetElBy:
    def __init__(self, driver):
        self.__driver = driver

    def css(self, selector):
        return self.__driver.find_element_by_css_selector(selector)

    def xpath(self, selector):
        return self.__driver.find_element_by_xpath(selector)

    def id(self, selector):
        return self.__driver.find_element_by_id(selector)

    def class_name(self, selector):
        return self.__driver.find_element_by_class_name(selector)

    def link(self, selector):
        return self.__driver.find_element_by_link_text(selector)

    def link_part(self, selector):
        return self.__driver.find_element_by_partial_link_text(selector)
