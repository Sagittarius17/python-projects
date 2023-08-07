import requests
from bs4 import BeautifulSoup
import os

# Make a request
page = requests.get("https://amazon.com")
soup = BeautifulSoup(page.content, 'html.parser')

# Locate the element that contains the image
image_element = soup.find("img")

if image_element is not None:
    # Get the URL of the image
    image_url = image_element["src"]

    # Download the image
    response = requests.get(image_url)

    # Create a file and write the image to it
    with open(os.path.join("/path/to/local/directory", "image.jpg"), "wb") as f:
        f.write(response.content)
    print("Download Complete!")
    
else:
    print("No image found.")