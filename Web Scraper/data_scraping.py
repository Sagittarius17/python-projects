import requests
from bs4 import BeautifulSoup
import csv

# Make a request to the website
url = 'https://www.nytimes.com/books/best-sellers/'
response = requests.get(url)

# Parse the HTML using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the data you want
books = soup.find_all('div', class_='css-3gxq11')

data = []
for book in books[:10]:
    title = book.find('h3', class_='css-5pe77f').get_text().strip()
    author = book.find('p', class_='css-hjukut').get_text().strip()
    data.append((title, author))

# Store the data in a CSV file
with open('nyt_bestsellers.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Author'])
    writer.writerows(data)
