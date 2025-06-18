from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
"""
启动浏览器
"""
def test():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com/advanced_search")
    check_input = driver.find_element(By.ID, "xX4UFf")
    email = "Pediatrician recommendations Indian USA"
    check_input.send_keys(email)
    check_input2 = driver.find_element(By.ID, "CwYCWc")
    email = "whatsapp.com"
    check_input2.send_keys(email)
    radio_button = driver.find_element(By.ID, "lr_button")
    radio_button.click()
'''
    try:
        language_option = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='option' and contains(text(), '阿拉伯语')]")))
        language_option.click()
    except Exception as e:
        print(f"元素未找到或超时: {e}")
    wait = WebDriverWait(driver, timeout=10)
'''
    options = radio_button.find_elements(By.XPATH, ".//div[@role='option']")
    for option in options:
        print("Option:", option.get_attribute("aria-label"))  # 可用于调试


# 等待元素出现并返回元素
element = wait.until(
    expected_conditions.presence_of_element_located((By.ID, "element_id"))
)
    radio_button2 = driver.find_element(By.XPATH, "//*[@id=\"cr_button\"]")
    radio_button2.click()
    radio_button2 = driver.find_element(By.XPATH, "//*[@id=\"as_qdr_button\"]")
    radio_button2.click()
    input("Press Enter to exit and close the browser...")
