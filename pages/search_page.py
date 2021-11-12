from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SearchPage(BasePage):
    def calc_on_search_page(self):
        self.browser.find_element(By.XPATH, '//div[text()="1"]').click()
        self.browser.find_element(By.XPATH, '//div[@aria-label="умножение"]').click()
        self.browser.find_element(By.XPATH, '//div[text()="2"]').click()
        self.browser.find_element(By.XPATH, '//div[@aria-label="вычитание"]').click()
        self.browser.find_element(By.XPATH, '//div[text()="3"]').click()
        self.browser.find_element(By.XPATH, '//div[@aria-label="сложение"]').click()
        self.browser.find_element(By.XPATH, '//div[text()="1"]').click()
        self.browser.find_element(By.XPATH, '//div[@aria-label="равно"]').click()
        