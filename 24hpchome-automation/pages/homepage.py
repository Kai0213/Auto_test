from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(driver)

    def search_product(self, query):
        search_input = (By.XPATH, '//*[@type="search"]')
        search_button = (By.XPATH, '//*[@data-regression="header_search_button"]')

        self.base_page.send_keys(search_input, query)
        self.base_page.click(search_button)

    def click_category(self, category_name):
        # 使用傳入的 category_name 建立動態 XPath
        category_locator = (By.XPATH, f'//*[text()="{category_name}"]')
        # 使用 base_page 的方法來點擊元素
        self.base_page.click(category_locator)