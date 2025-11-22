from bs4 import BeautifulSoup
import requests
import lxml
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()


url="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
email = os.environ.get("EMAIL_ADDRESS")
password= os.environ.get("EMAIL_PASSWORD")
smtp= os.environ.get("SMTP_ADDRESS")
headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
  }


response = requests.get(url, headers= headers)
url_text = response.text

soup= BeautifulSoup(url_text, "html.parser")

price = soup.find(class_="a-offscreen").getText()

price_full = price.split("$")[1]

final_price = float(price_full)
print(final_price)

title = soup.find(name="span", id= "productTitle")
email_subject = title.getText()

if final_price < 100:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.ehlo()
        connection.starttls(context=ssl.create_default_context())
        connection.login(user="gabpythontest@gmail.com", password="zgewdhzrbvtyhzza")
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg=f"Amazon Price Alert!\n\n {email_subject}is on sale for ${final_price}")
