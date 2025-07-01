from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, timeout=10):
        """
        初始化 BasePage 对象
        :param driver: Selenium WebDriver 实例
        :param timeout: 默认等待超时时间（秒）
        """
        self.driver = driver
        self.timeout = timeout


    def wait_for_element(self, locator):
        """
        等待元素出现在 DOM 中并返回 WebElement（不保证可见）
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                expected.presence_of_element_located(locator)
            )
        except TimeoutException:
            print(f"[ERROR] 等待元素失败：{locator}")
            return None

    def wait_for_visible(self, locator):
        """
        等待元素可见（displayed 为 True）
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                expected.visibility_of_element_located(locator)
            )
        except TimeoutException:
            print(f"[ERROR] 元素不可见：{locator}")
            return None


