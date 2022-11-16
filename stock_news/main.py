import requests
import os
import smtplib
# from newsapi import articles
NEWS_API = "https://newsapi.org/v2/everything"
N_API_KEY = os.environ.get("N_API_KEY")
S_API_KEY = os.environ.get("S_API_KEY")
STOCK_API = "https://www.alphavantage.co/query"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
USER_NAME = os.environ.get("USER_NAME")
APP_PASS = os.environ.get("APP_PASS")
email_list = ["****@gmail.com", "***@gmail.com"]

n_params = {
    "q": "tesla",
    "sortBy": "relevancy",
    # "sources": 'bbc-news,the-verge',
    # "category": "business",
    "language": "en",
    # "country": "us",
    "pageSize": 3,
    "apiKey": N_API_KEY
}
s_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": S_API_KEY
}


def send_email(email, message):
    # print(message)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER_NAME, password=APP_PASS)
        connection.sendmail(from_addr=USER_NAME,
                            to_addrs=email,
                            msg=f"Subject:Stock Alert: {STOCK} ,"
                                f" \n\n{message}".encode("utf8"))


def get_percent_change(lastdy, daybflastdy):
    lastdy_val = float(lastdy)
    daybflastdy_val = float(daybflastdy)
    is_increase = "🔻"
    print(daybflastdy_val)
    print(lastdy_val)
    change = 0
    if daybflastdy_val > lastdy_val:
        change = round((abs(lastdy_val - daybflastdy_val) / lastdy_val) * 100)
    else:
        is_increase = "🔺"
        change = round((abs(lastdy_val - daybflastdy_val) / lastdy_val) * 100)
    return change, is_increase


stock_response = requests.get(STOCK_API, params=s_params)
stock_response.raise_for_status()

value_list = list(stock_response.json()["Time Series (Daily)"].values())
values = get_percent_change(value_list[0]["4. close"], value_list[1]["4. close"])

if values[0] > 1:
    news_response = requests.get(NEWS_API, params=n_params)
    news_response.raise_for_status()
    message = f"hey! \n\nCheck out latest news of {STOCK} stock! \n\n"
    for article in news_response.json()["articles"]:
        message += f"TSLA: {values[0]}%{values[1]}\n Headline: {article['title']} \n Brief: {article['description']}" \
                   f" \nBrief: {article['description']} \n\n"
        print(f"TSLA: {values[0]}%{values[1]}\n")
        print(f"Headline: {article['title']} \n")
        print(f"Brief: {article['description']} \n")
        print("*************************\n")
    message += "Best Regards \nStock alert App"
    for email in email_list:
        send_email(email, message)


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

