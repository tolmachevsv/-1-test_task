import time

from pages.search_page import SearchPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def start_searching_for_calc(self):
        search_str = self.browser.find_element(By.XPATH, '//input[@title="Поиск"]')
        search_str.send_keys('Калькулятор')
        time.sleep(2)

    def go_to_searching_page(self):
        start_searching = self.browser.find_element(By.XPATH, '//input[@aria-label="Поиск в Google"]')
        start_searching.click()
        return SearchPage(browser=self.browser, url=self.browser.current_url)
        