from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseTest:
    def __init__(self, driver):
        """
        Initialize the BaseTest with a WebDriver instance.

        :param driver: WebDriver instance
        """
        self.driver = driver

    def find_element(self, *locator):
        """
        Find a single element after waiting for it to be present in the DOM.

        :param locator: Locator tuple (By.<method>, value)
        :return: WebElement found
        """
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def find_elements(self, *locator):
        """
        Find multiple elements after waiting for them to be present in the DOM.

        :param locator: Locator tuple (By.<method>, value)
        :return: List of WebElements found
        """
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    def open(self, url):
        """
        Open a URL in the current browser window.

        :param url: URL to open
        """
        self.driver.get(url)

    def click(self, *locator):
        """
        Click on an element located by the given locator.

        :param locator: Locator tuple (By.<method>, value)
        """
        self.find_element(*locator).click()

    def double_click(self, element):
        """
        Double click on a given WebElement.

        :param element: WebElement to double click
        """
        from selenium.webdriver import ActionChains
        action = ActionChains(self.driver)
        action.double_click(element).perform()

    def clear_and_send_keys(self, element, keys):
        """
        Clear the input field of a WebElement and send keys to it.

        :param element: WebElement input field to clear and send keys to
        :param keys: Keys to send to the input field
        """
        element.clear()
        element.send_keys(keys)
