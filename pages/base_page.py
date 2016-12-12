from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    search_input = '//*[@id="search_text"]'
    search_button = '//*[@id="search_submit"]'
    list_view = '//*[@id="output_view_mode_0"]'
    gallery_view = '//*[@id="output_view_mode_1"]'
    count_of_selected = '//*[@id="favorite_products"]/a/span[2]'
    comparison_link = '//*[@id="favorite_products"]/a'

    def __init__(self, driver):
        self.driver = driver
        self.url = ' http://prom.ua'

    def navigate(self):
        self.driver.get(self.url)

    def go_to_comparison(self):
        self.click_on_the_object(self.comparison_link)

    def search_good(self, goods):
        self.enter_text_into_field(self.search_input, goods)
        self.click_on_the_object(self.search_button)

    def select_gallery_view(self):
        self.click_on_the_object(self.gallery_view)

    def select_list_view(self):
        self.click_on_the_object(self.list_view)

    def return_count_of_goods_in_selected(self):
        return int(self.driver.find_element_by_xpath(self.count_of_selected).text)

    def enter_text_into_field(self, xpath, text):
        self.wait_until_object_appears(xpath)
        field = self.driver.find_element_by_xpath(xpath)
        field.send_keys(text)

    def click_on_the_object(self, xpath):
        self.wait_until_object_appears(xpath)
        elem = self.driver.find_element_by_xpath(xpath)
        elem.click()

    def hover_element(self, xpath):
        self.wait_until_object_appears(xpath)
        element = self.driver.find_element_by_xpath(xpath)
        hov = ActionChains(self.driver).move_to_element(element)
        hov.perform()

    def wait_until_object_appears(self, xpath):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print('Element is not exist on page, xpath '+xpath)
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print('Element is not visible on page, xpath ' + xpath)
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
        except TimeoutException:
            print('Element is not clickable on page, xpath ' + xpath)
