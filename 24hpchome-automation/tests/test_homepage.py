import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.homepage import HomePage
import allure

@pytest.fixture
def driver():
    # Setup ChromeDriver
    service = Service(ChromeDriverManager().install())
    #service = Service(executable_path='./chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    
    # Navigate to site
    driver.get('https://24h.pchome.com.tw/')
    
    yield driver
    
    # Teardown
    driver.quit()

def test_homepage_search(driver):
    home_page = HomePage(driver)
    home_page.search_product('iPhone')
    
    assert 'iPhone' in driver.title

def test_homepage_category_navigation(driver):
    # 測試主要分類選單導航
    home_page = HomePage(driver)
    home_page.click_category("3C")  # 需要在 HomePage 類中實現此方法
    assert "3C" in driver.title