import requests
from bs4 import BeautifulSoup

def get_links(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # If the GET request is successful, the status code will be 200
    if response.status_code == 200:
        # Get the content of the response
        page_content = response.content

        # Create a BeautifulSoup object and specify the parser
        soup = BeautifulSoup(page_content, 'html.parser')

        # Find all the anchor tags in the HTML
        # Extract the href attribute and add it to a list
        links = [a['href'] for a in soup.find_all('a', href=True)]
        
        return links
    else:
        return f"Failed to retrieve the webpage. Status Code: {response.status_code}"

# Example usage
url = "https://shuvendusingha.onrender.com"
links = get_links(url)

if isinstance(links, list):
    for link in links:
        print(link)
else:
    print(links)
