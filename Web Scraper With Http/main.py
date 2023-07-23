import http.client
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def get_html(url):
    parsed_url = urlparse(url)
    conn = http.client.HTTPSConnection(parsed_url.netloc)
    conn.request("GET", parsed_url.path)
    response = conn.getresponse()
    html = response.read().decode('utf-8')
    conn.close()
    return html

def get_links(url):
    html_content = get_html(url)
    soup = BeautifulSoup(html_content, 'html.parser')
    links = [a.get('href') for a in soup.find_all('a')]
    return links

# Example usage
url = "https://shuvendusingha.onrender.com/"
links = get_links(url)
for link in links:
    print(link)
