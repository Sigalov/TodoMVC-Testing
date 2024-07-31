import pytest
from selenium import webdriver
from pages.todo_page import TodoPage
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """
    Initialize a WebDriver instance.

    Yields:
        WebDriver: An instance of the Chrome WebDriver.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--remote-debugging-port=9222")

    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def todo_page(driver):
    """
    Initialize the TodoPage object.

    Args:
        driver (WebDriver): An instance of the Chrome WebDriver.

    Returns:
        TodoPage: An instance of the TodoPage object.
    """
    page = TodoPage(driver)
    page.open()
    return page
