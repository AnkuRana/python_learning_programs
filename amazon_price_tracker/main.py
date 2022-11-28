import requests
import smtplib
from bs4 import BeautifulSoup
import os

url_zon = "https://www.amazon.in/JIO-HOME-GYM-Power-Medium/dp/B07NJLVJV7/?_encoding=UTF8" \
      "&pd_rd_w=aYaJi&content-id=amzn1.sym.1f592895-6b7a-4b03-9d72-1a40ea8fbeca&pf_rd_" \
      "p=1f592895-6b7a-4b03-9d72-1a40ea8fbeca" \
      "&pf_rd_r=00ECJDP2ZSQM5HKS9J9M&pd_rd_wg=q3GQ2&pd_rd_r=" \
      "b6c32af1-19ea-4ad7-8a02-85cc20a51507&ref_=pd_gw_ci_mcx_mr_hp_atf_m"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                  "like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
USERNAME = "********@gmail.com"  # add senders email
APP_PASSWORD = os.environ.get("EMAIL_PASS")
WANT_PRICE = 15000
MESSAGE = f"Hey!,\nPrice of....\n\n{url_zon}\n\nhas came down to {WANT_PRICE}." \
          f"\n\nIt is best time to buy now!\n\nBest Regards\nAmit Rana"


def send_email(email, message):
    # print(message)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=APP_PASSWORD)
        connection.sendmail(from_addr=USERNAME,
                            to_addrs=email,
                            msg=f"Subject:Price tracker"
                                f"\n\n{message}".encode("utf8"))


response = requests.get(url=url_zon, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
get_divs = soup.find(name="span", class_="a-price-whole")
prod_price = get_divs.getText().strip(".").split(",")
prod_price = float(prod_price[0] + prod_price[1])

if prod_price <= WANT_PRICE:
    send_email("*****@gmail.com", MESSAGE)
# get_divs = soup.find_all(name="div", class_="a-spacing-none")

# for div in get_divs:
#     print(div.find(name="span", class_="a-price-whole"))
