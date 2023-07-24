from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# you need to replace 'your_chrome_driver_path' with the actual path where you have kept the Chrome driver.
driver = webdriver.Chrome('your_chrome_driver_path')

# We are telling Selenium to get the page of the following url
driver.get('http://www.example.com')

# After this line is executed, Chrome Browser will be launched and it will load the URL that we passed.
try:
    # Wait until the "article" elements are loaded
    articles = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'article')))

    # Iterating through each article and printing its title
    for article in articles:
        print(article.find_element_by_class_name('title').text)

finally:
    # Closing the driver after use
    driver.quit()
