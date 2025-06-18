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

    def click(self, locator):
        """
        等待元素可点击并点击
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                expected.element_to_be_clickable(locator)
            )
            element.click()
        except TimeoutException:
            print(f"[ERROR] 无法点击元素：{locator}")

    def type(self, locator, text):
        """
        输入文本（等待可见）
        """
        element = self.wait_for_visible(locator)
        if element:
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        """
        获取元素文本
        """
        element = self.wait_for_visible(locator)
        return element.text if element else ""

    def send_key(self, locator, key):
        """
        向元素发送单个键（如 Keys.ENTER）
        """
        element = self.wait_for_visible(locator)
        if element:
            element.send_keys(key)

    def find(self, locator):
        """
        查找元素（presence）
        """
        return self.driver.find_element(*locator)
    
    def open_url(self, url, wait_condition=None):
        """
        打开指定的网页
        :param url: 要访问的 URL
        :param wait_condition: 可选的等待条件（如 expected.title_contains("xxx")）
        """
        try:
            self.driver.get(url)
            if wait_condition:
                WebDriverWait(self.driver, self.timeout).until(wait_condition)
        except TimeoutException:
            print(f"[ERROR] 打开页面超时：{url}")

