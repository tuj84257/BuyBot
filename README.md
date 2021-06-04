# BuyBot

Just a simple Python bot that uses Selenium to buy stuff from BestBuy.

## Things you need to install before proceeding

Assuming you already have a BestBuy account, and have added a card under your account, install these:

1. Python 3.8
2. Selenium - `pip install selenium`
3. Google Chrome
4. [ChromeDriver](https://chromedriver.chromium.org/downloads) - make sure you download the driver that is compatible with the version of Google Chrome, and then unzip the `.exe` file it to a location in your computer.

## Running the bot

1. Go to the `BuyBot` directory.

2. Open `settings.py`, and change `CHROME_DRIVER_PATH`, `BEST_BUY_ITEM_URL`, `BEST_BUY_EMAIL`, `BEST_BUY_PASSWORD`, and `CVV` according to your case.
3. Run the bot - `python run_bot.py`