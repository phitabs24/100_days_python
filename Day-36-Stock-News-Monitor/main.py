import requests
from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = os.environ.get("ALPHA_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
MY_EMAIL = os.environ.get("GMAIL_USERNAME")
MY_PASSWORD = os.environ.get("GMAIL_PASSWORD")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

email = "phitechinc@gmail.com"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": ALPHA_API_KEY,
}
# 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
data = requests.get(STOCK_ENDPOINT, params=stock_params).json()["Time Series (Daily)"]
closing_prices = [float(value["4. close"]) for (key, value) in data.items()]
yesterday_closing_price = closing_prices[0]

# 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing_price = closing_prices[1]

# 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
positive_difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
# 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_diff = (positive_difference / yesterday_closing_price) * 100
# 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_diff > 5:

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

    # 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    news_params = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    news = requests.get(NEWS_ENDPOINT, params=news_params).json()["articles"][:3]

    # 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # 8. - Create a new list of the first 3 articles' headline and description using list comprehension.
    # Optional Format the message like this:
    formatted_articles = [
        f"TSLA: [sign]{round(percent_diff)}%\nHeadline:{article["title"]}.\nBrief:{article["description"]}" for article
        in news]

    # 9. - Send each article as a separate message via Twilio.
    for message in formatted_articles:
        if yesterday_closing_price > day_before_yesterday_closing_price:
            message = message.replace("[sign]", "🔺")
        else:
            message = message.replace("[sign]", "🔻")

        msg = MIMEText(message)
        msg['Subject'] = "Stock News"
        msg['From'] = MY_EMAIL
        msg['To'] = email

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(MY_EMAIL, MY_PASSWORD)  # Replace with your Gmail password
        server.sendmail(MY_EMAIL, email, msg.as_string())
        server.quit()
