from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com/advanced_search")

wait = WebDriverWait(driver, 5)

# 1. 找到下拉按钮并点击展开
lr_button = wait.until(EC.element_to_be_clickable((By.ID, "lr_button")))
lr_button.click()
time.sleep(0.01)  # UI 渲染动画

# 2. 使用键盘向下，直到 aria-activedescendant == ":19"
target_id = ":19"
max_attempts = 100  # 防止死循环
attempts = 0

while attempts < max_attempts:
    current_id = lr_button.get_attribute("aria-activedescendant")
    if current_id == target_id:
        print(f"当前 ID: {current_id}, {attempts}")
        break
    lr_button.send_keys(Keys.ARROW_DOWN)
    attempts += 1

# 3. 确认选择
lr_button.send_keys(Keys.ENTER)

# 1. 找到下拉按钮并点击展开
cr_button = wait.until(EC.element_to_be_clickable((By.ID, "cr_button")))
cr_button.click()
time.sleep(0.01)  # UI 渲染动画

# 2. 使用键盘向下，直到 aria-activedescendant == ":4y"
target_id = ":4y"
max_attempts = 200  # 防止死循环
attempts = 0

while attempts < max_attempts:
    current_id = cr_button.get_attribute("aria-activedescendant")
    if current_id == target_id:
        print(f"当前 ID: {current_id}, {attempts}")
        break
    cr_button.send_keys(Keys.ARROW_DOWN)
    attempts += 1

# 3. 确认选择
cr_button.send_keys(Keys.ENTER)
input("等待")
