import requests
from newsapi import NewsApiClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "da68e365cc074e4e9c9d122aadf7b46b"
ALPHA_API = "N6P9OZXGMWK4VW94"

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API
}

NEWS_PARAMS = {
    "apikey": NEWS_API,
    "qInTitle": COMPANY_NAME
}

# STEP 1: Use https://www.alphavantage.co/query
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the
# two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yesterday's closing stock price.

response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday = data_list[0]
day_before_yesterday = data_list[1]
yesterday_closing = yesterday["4. close"]
day_before_yesterday_closing = day_before_yesterday["4. close"]
difference = abs(float(yesterday_closing) - float(day_before_yesterday_closing))
diff_percent = (difference / float(yesterday_closing)) * 100
# print(diff_percent)

# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator

if diff_percent > 3:
    news_response = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
    articles = news_response.json()["articles"]
    print(articles)

# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file
 by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the 
 coronavirus market crash.
"""
