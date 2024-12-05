# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 19:51:11 2024

@author: Yash Jondhale
"""


from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Setup Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service("C:/Users/91927/Dropbox/PC/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")  # Replace with the path to your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

#load the required web page link to the chrome page
driver.get('https://www.naukri.com/data-science-jobs-in-india-2?k=data+science&l=india&experience=0')

# Scroll down to load more reviews (if necessary)

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
while True:
    # Get the page source and parse it with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(soup.prettify())
    
    reviews = soup.find_all('a', {'class': 'title'})
    
    review_title=[]
    for i in range(0,len(reviews)):
        review_title.append(reviews[i].get_text())
    review_title
    #The strip('\n') method is used to remove leading or trailing 
    #newline characters.
    review_title[:]=[r.strip('\n') for r in review_title]
    review_title
    len(review_title)
    
    JD = soup.find_all('div', {'class': 'row4'})
    
    job_desc=[]
    for i in range(0,len(reviews)):
        job_desc.append(JD[i].get_text())
    job_desc
    job_desc[:]=[r.strip('\n') for r in job_desc]
    job_desc
    len(job_desc)
    fields = soup.find_all('div', {'class': 'row5'})
    
    
    # Assuming 'soup' is already created and contains the parsed HTML
    
    # Find all divs containing the company data (replace 'row5' with the correct class if needed)
    companies = soup.find_all('div', {'class': 'row5'})
    
    # Initialize a single variable to store the results for all companies
    all_companies_data = {}
    
    # Regular expression to match the content inside the <li> tag
    pattern = r'<li.*?>(.*?)</li>'
    
    # Iterate through each company block (div with class 'row5')
    for idx, company in enumerate(companies):
        # Convert each company block to a string and parse it again with BeautifulSoup
        company_soup = BeautifulSoup(str(company), 'html.parser')
        
        # Find all <li> tags with class 'dot-gt tag-li' inside each company block
        li_tags = company_soup.find_all('li', class_='dot-gt tag-li')
        
        # List to store the results for the current company
        results = []
        
        # Extract the text from each <li> tag
        for tag in li_tags:
            match = re.search(pattern, str(tag))  # Convert each tag to a string and search for the pattern
            if match:
                results.append(match.group(1))  # Append the text content to the results list
        
        # Store the data for the current company in the dictionary
        all_companies_data[f'Company_{idx+1}'] = results
        
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@class='styles_btn-secondary__2AsIP']"))
            )
                   
            # Click the "Next" button to go to the next page
            next_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error or no more pages: {e}")
            break

# Store the results in a single variable
scraped_data = all_companies_data

# Print the scraped data for all companies
print(scraped_data)
len(scraped_data)     


#Storing the data into csv file.
import pandas as pd

# Assuming review_title and job_desc are lists of equal length
print(scraped_data)  # Check the contents of scraped_data
len(all_companies_data)
# Convert the 'scraped_data' dictionary to a list, extracting just the field lists
fields_list = [', '.join(value) for value in scraped_data.values()]  # Flatten into strings

# Check if the lengths of review_title, job_desc, and fields_list are the same
print(len(review_title), len(job_desc), len(fields_list))
import pandas as pd
df = pd.DataFrame()
df['Review_title']= review_title
df['Job Description']= job_desc
df['fields']= all_companies_data

df

df.to_csv("I:/My Drive/study/Final Year/Final_year_Project/test/naukri1.csv")
driver.quit()
