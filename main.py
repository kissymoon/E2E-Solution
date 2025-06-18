import tkinter as tk
from Gui_Object_Model.Control_gui import ControlGui
from Page_Object_Model.adv_Search_Page import AdvsPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
        
 
if __name__ == "__main__":
    app = ControlGui()
    app.run()
    
    # service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service)

    # driver = webdriver.Chrome()
    # driver.maximize_window()
    # page = AdvsPage(driver, app.result)
    # page.pull()
