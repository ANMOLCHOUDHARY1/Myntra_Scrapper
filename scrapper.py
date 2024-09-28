import time
from selenium import webdriver
import urllib.request
import os
import json
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  # Import By

# Initialize a global image counter
image_counter = 0
max_images = 2  # Stop after collecting 500 images

def retrieve_links(search_string):
    links = []
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://www.myntra.com/')
    time.sleep(5)
    
    # Updated methods using By.CLASS_NAME
    driver.find_element(By.CLASS_NAME, 'desktop-searchBar').send_keys(search_string)
    driver.find_element(By.CLASS_NAME, 'desktop-submit').click()
    
    while True:
        time.sleep(5)
        for product_base in driver.find_elements(By.CLASS_NAME, 'product-base'):
            links.append(product_base.find_element(By.XPATH, './a').get_attribute("href"))
        try:
            driver.find_element(By.CLASS_NAME, 'pagination-next').click()
        except:
            driver.close()
            driver.quit()
            return links

def get_product_meta_data(link, base):
    global image_counter
    
    if image_counter >= max_images:  # Stop if max images are collected
        print(f"Reached the limit of {max_images} images.")
        return
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) 
    driver.get(link)
    metadata = dict()
    metadata['link'] = link
    while True:
        try:
            metadata['title'] = driver.find_element(By.CLASS_NAME, 'pdp-title').get_attribute("innerHTML")
            break
        except:
            pass
    metadata['name'] = driver.find_element(By.CLASS_NAME, 'pdp-name').get_attribute("innerHTML")
    metadata['price'] = driver.find_element(By.CLASS_NAME, 'pdp-price').find_element(By.XPATH, './strong').get_attribute("innerHTML")
    metadata['specifications'] = dict()
    try:
        driver.find_element(By.CLASS_NAME, 'index-showMoreText').click()
    except:
        pass
    for index_row in driver.find_element(By.CLASS_NAME, 'index-tableContainer').find_elements(By.CLASS_NAME, 'index-row'):
        metadata['specifications'][index_row.find_element(By.CLASS_NAME, 'index-rowKey').get_attribute("innerHTML")] = index_row.find_element(By.CLASS_NAME, 'index-rowValue').get_attribute("innerHTML")
    metadata['productId'] = driver.find_element(By.CLASS_NAME, 'supplier-styleId').get_attribute("innerHTML")
    
    try:
        os.mkdir("data")
    except:
        pass
    try:
        os.mkdir(os.path.join("data", base))
    except:
        pass
    try:
        os.mkdir(os.path.join("data", base, metadata['productId']))
        os.mkdir(os.path.join("data", base, metadata['productId'], 'images'))
    except:
        driver.close()
        driver.quit()

    itr = 1
    for image_tags in driver.find_elements(By.CLASS_NAME, 'image-grid-image'):
        if image_counter >= max_images:  # Check if we've hit the limit during image saving
            print(f"Reached the limit of {max_images} images.")
            driver.close()
            driver.quit()
            return
        
        image_path = os.path.join("data", base, metadata['productId'], 'images', str(itr) + ".jpg")
        urllib.request.urlretrieve(image_tags.get_attribute('style').split("url(\"")[1].split("\")")[0], image_path)
        itr += 1
        image_counter += 1  # Increment the image counter
        
        print(f"Image {image_counter} saved.")
        
        if image_counter >= max_images:  # Stop once max images are collected
            break

    with open(os.path.join("data", base, metadata['productId'], 'metadata.json'), 'w') as fp:
        json.dump(metadata, fp)
    
    driver.close()
    driver.quit()

if __name__ == "__main__":
    try:
        file_ = open("clothings.txt", "r")
        search_strings = file_.readlines()
        file_.close()
        for string in search_strings:
            search_string = string.strip()  # Strip newline characters
            links = list(set(retrieve_links(search_string)))
            for link in links:
                get_product_meta_data(link, search_string)
                if image_counter >= max_images:  # Break the loop once the image limit is reached
                    break
            if image_counter >= max_images:  # Break the loop if the image limit is reached
                break
        print(f"Scraping completed. {image_counter} images collected.")
    except KeyboardInterrupt:
        print("\nScraper interrupted by user. Data collected so far is saved.")
    except Exception as e:
        print(f"An error occurred: {e}")
