import requests
from bs4 import BeautifulSoup

url = "example.com"  # Replace with the actual URL of the coupon website

# Send a GET request to the coupon website
response = requests.get(url)

# Parse the HTML content of the webpage using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Inspect the HTML structure of the webpage to locate the coupon information
coupons = soup.find_all("div", class_="coupon")  # Example: searching for div elements with class="coupon"

# Process and display the extracted coupon information
if coupons:
    print("Coupons found:")
    for coupon in coupons:
        code = coupon.find("span", class_="example-coupon").text.strip()
        description = coupon.find("p", class_="example-coupon-description").text.strip()
        print(f"Coupon Code: {code}")
        print(f"Description: {description}")
        print("-" * 20)
else:
    print("No coupons found on the website.")
