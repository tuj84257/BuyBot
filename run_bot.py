from settings import (
    CHROME_DRIVER_PATH, BEST_BUY_ITEM_URL,
    BEST_BUY_EMAIL, BEST_BUY_PASSWORD, CVV
)

from utils import (
    ChromeDriver, BEST_BUY_CART_URL, add_to_cart_button_CSS_class,
    checkout_button_XPATH, email_field_id,
    password_field_id, sign_in_button_XPATH,
    store_pickup_location_class, store_pickup_address_class,
    cvv_field_id, place_order_button_class
)

# start chrome driver
chrome_driver_object = ChromeDriver(CHROME_DRIVER_PATH)
chrome_driver = chrome_driver_object.start_chrome_driver()

# go to the item's URL
chrome_driver.get(BEST_BUY_ITEM_URL)

# start placing the order
while True:
    # try to get the add to cart button
    try:
        add_to_cart_button =  chrome_driver_object.get_element(
            chrome_driver=chrome_driver,
            # wait 10 seconds until the button becomes clickable
            wait_time=10,
            action='clickable',
            css_selector=add_to_cart_button_CSS_class
        )
        print('Found add to cart button!')
    # otherwise, refresh the driver, and continue to the next iteration
    except:
        print('Did not find add to cart button!')
        chrome_driver.refresh()
        continue
    # begin the checkout process
    try:
    # add the item to the cart
        add_to_cart_button.click()
        print('Added the item to the cart!')
        # go to the cart
        chrome_driver.get(BEST_BUY_CART_URL)
        checkout_button = chrome_driver_object.get_element(
            chrome_driver=chrome_driver,
            wait_time=10,
            action='present',
            xpath=checkout_button_XPATH
        )
        # click the checkout button
        checkout_button.click()
        print('Beginning checkout...')
        email_field = chrome_driver_object.get_element(
            chrome_driver=chrome_driver,
            wait_time=10,
            action='present',
            css_selector=email_field_id
        )
        password_field = chrome_driver_object.get_element(
            chrome_driver=chrome_driver,
            wait_time=10,
            action='present',
            css_selector=password_field_id
        )
        sign_in_button = chrome_driver_object.get_element(
            chrome_driver=chrome_driver,
            wait_time=10,
            action='present',
            xpath=sign_in_button_XPATH
        )
        # enter email
        email_field.send_keys(BEST_BUY_EMAIL)
        # enter password
        password_field.send_keys(BEST_BUY_PASSWORD)
        # sign in
        sign_in_button.click()
        print('Signed in.')
        cvv_field = chrome_driver_object.get_element(
            chrome_driver=chrome_driver,
            wait_time=10,
            action='present',
            css_selector=cvv_field_id
        )
        place_order_button = chrome_driver_object.get_element(
            chrome_driver=chrome_driver,
            wait_time=0,
            action='present',
            css_selector=place_order_button_class
        )
        print('---------------------')
        print('Store pickup information:')
        print(chrome_driver.find_element_by_class_name(store_pickup_location_class).text)
        print(chrome_driver.find_element_by_class_name(store_pickup_address_class).text)
        print('---------------------')
        # Enter CVV information
        cvv_field.send_keys(CVV)
        print('Entered CVV information.')
        # Place the order
        place_order_button.click()
        break
    # Handle any error here
    except:
        chrome_driver.get(BEST_BUY_ITEM_URL)
        print('Error detected - restarting bot!')
        continue

print('Successfully placed the order.')
