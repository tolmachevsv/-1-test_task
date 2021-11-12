from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.main_page import MainPage

class TestMainPage():

    def setup(self):
        self.browser = webdriver.Chrome()

    def teardown(self):
        self.browser.quit()

    def test_memory_and_result_calc(self):
        url = 'http://google.com'
        required_calculation = '1 × 2 - 3 + 1 ='
        google_main_page = MainPage(self.browser, url)
        google_main_page.open()
        google_main_page.start_searching_for_calc()
        searching_page = google_main_page.go_to_searching_page()
        searching_page.calc_on_search_page()
        memory_string = self.browser.find_element(By.XPATH, "//span[text()='1 × 2 - 3 + 1 =']")
        result = self.browser.find_element(By.ID, 'cwos')
        assert memory_string.text == required_calculation
        assert result.text == '0'
