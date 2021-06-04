from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

# define some variables
BEST_BUY_CART_URL = 'https://www.bestbuy.com/cart'
add_to_cart_button_CSS_class = '.add-to-cart-button'
checkout_button_XPATH = '//*[@id="cartApp"]/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[3]/div/div[1]/button'
email_field_id = '#fld-e'
password_field_id = '#fld-p1'
sign_in_button_XPATH = '/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/form/div[3]/button'
store_pickup_location_class = 'ispu-summary__store-name'
store_pickup_address_class = 'ispu-summary__store-link'
cvv_field_id = '#credit-card-cvv'
place_order_button_class = '.button__fast-track'

# The ChromeDriver class
class ChromeDriver:
    def __init__(self, path):
        self.path = path

    def start_chrome_driver(self):
        return webdriver.Chrome(self.path)

    def get_element(self, chrome_driver, wait_time, action, css_selector=None, xpath=None):
        if css_selector is not None:
            if action == 'clickable':
                return WebDriverWait(chrome_driver, wait_time).until(
                    expected_conditions.element_to_be_clickable(
                        (By.CSS_SELECTOR, css_selector)
                    )
                )
            if action == 'present':
                return WebDriverWait(chrome_driver, wait_time).until(
                    expected_conditions.presence_of_element_located(
                        (By.CSS_SELECTOR, css_selector)
                    )
                )
        if xpath is not None:
            if action == 'clickable':
                return WebDriverWait(chrome_driver, wait_time).until(
                    expected_conditions.element_to_be_clickable(
                        (By.XPATH, xpath)
                    )
                )
            if action == 'present':
                return WebDriverWait(chrome_driver, wait_time).until(
                    expected_conditions.presence_of_element_located(
                        (By.XPATH, xpath)
                    )
                )
