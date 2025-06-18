from .Basic_Page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class AdvsPage(BasePage):
    def __init__(self, driver, s_value, timeout=5):
        """
        初始化 BasePage 对象
        :param driver: Selenium WebDriver 实例
        :param timeout: 默认等待超时时间（秒）
        """
        self.driver = driver
        self.path = "https://www.google.com/advanced_search"
        self.value = s_value
        self.timeout = timeout
        self.page_source = self.driver.page_source

    # 高级搜索具体实现    
    def adv(self):
        # 打开“高级搜索”
        self.open_url(self.path)
        # 关键字与必包含
        self.send_key((By.ID,"xX4UFf"), self.value['keywords'][0])
        self.send_key((By.ID,"CwYCWc"), self.value['must_include'])
        # 语言与地区
        self.while_send("lr_button", ":19")
        self.while_send("cr_button", ":4y")
        # 时间
        for i in range(self.value['time_range']):
            self.send_key((By.ID, "as_qdr_button"),Keys.ARROW_DOWN)
        self.send_key((By.ID, "as_qdr_button"), Keys.ENTER)    
        # 域名
        self.send_key((By.XPATH, "//*[@id=\"NqEkZd\"]"), self.value['domain'])
        # 提交
        time.sleep(1)
        self.click((By.XPATH, "//*[@id=\"s1zaZb\"]/div[5]/div[8]/div[2]/input[2]"))
        # 等待返回
        time.sleep(2)
        print(self.page_source)

    # duckgo引擎    
    def duck_adv(self):
        self.path = "https://duckduckgo.com"
        self.open_url(self.path)
        search_value = f"site:facebook.com \"{self.value['keywords'][0]}\" \"whatsapp.com\""
        print(search_value)
        self.send_key((By.ID, "searchbox_input"), search_value)
        self.click((By.XPATH, "//*[@id=\"searchbox_homepage\"]/div/div/div/button[2]"))
        time.sleep(5)
        print(self.driver.page_source)
        

    # 下拉框循环    
    def while_send(self, by_id, target_id,):  
        button = (By.ID, by_id)
        self.click((By.ID, by_id))
        max_attempts = 200  # 防止死循环
        attempts = 0
        while attempts < max_attempts:
            time.sleep(0.02)
            current_id = self.find(button).get_attribute("aria-activedescendant")
            if current_id == target_id:
                print(f"当前 ID: {current_id}, {attempts}")
                self.send_key(button, Keys.ENTER)
                break
            self.send_key(button, Keys.ARROW_DOWN)
            attempts += 1
            
    def analysis(self, source):
        pass

    # 拉取        
    def pull(self):
        self.duck_adv()
        input("等待...")
