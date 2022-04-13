import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

class TestLanguage():
    def test_button_add_to_basket_is_on_page(self, browser):
        browser.get(link)
        time.sleep(10)
        button_add_to_basket_visible = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.btn-add-to-basket'))
        )

        assert button_add_to_basket_visible.is_displayed()

