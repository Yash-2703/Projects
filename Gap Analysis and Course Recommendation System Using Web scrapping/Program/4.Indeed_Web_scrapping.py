
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Setup Selenium WebDriver
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
service = Service("C:/Users/91927/Dropbox/PC/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")  # Replace with the path to your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

#load the required web page link to the chrome page
driver.get('https://in.indeed.com/jobs?q=data+science&l=India&ts=1726748818754&from=searchOnHP&rq=1&rsIdx=0&fromage=last&vjk=e15896c02fddb798')

# Scroll down to load more reviews (if necessary)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Get the page source and parse it with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.prettify())


# finding the required section of web page using inspect and assiging the 
# section of the tag to fetch the data.

#<div id="customer_review-R3K7YOQ2DN24JP" class="a-section celwidget" data-csa-c-id="hs27is-gysrxj-lsp6cn-quy7dm" data-cel-widget="customer_review-R3K7YOQ2DN24JP"><div data-hook="genome-widget" class="a-row a-spacing-mini"><a href="/gp/profile/amzn1.account.AE2UZEUGFNJ2FJR7MXA6EM5DZOZA/ref=cm_cr_dp_d_gw_tr?ie=UTF8" class="a-profile" data-a-size="small"><div aria-hidden="true" class="a-profile-avatar-wrapper"><div class="a-profile-avatar"><img src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png" class="" data-src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"><noscript><img src="https://images-na.ssl-images-amazon.com/images/S/amazon-avatars-global/default._CR0,0,1024,1024_SX48_.png"/></noscript></div></div><div class="a-profile-content"><span class="a-profile-name">Caleb Silva</span></div></a></div><div class="a-row"><a data-hook="review-title" class="a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold" href="/gp/customer-reviews/R3K7YOQ2DN24JP/ref=cm_cr_dp_d_rvw_ttl?ie=UTF8&amp;ASIN=B0CSGWXVBN"><i data-hook="review-star-rating" class="a-icon a-icon-star a-star-5 review-rating"><span class="a-icon-alt">5.0 out of 5 stars</span></i><span class="a-letter-space"></span>
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Extract names of users 
reviews = soup.find_all('div', {'class': 'css-dekpa e37uo190'})
review_title=[]
for i in range(0,len(reviews)):
    review_title.append(reviews[i].get_text())
review_title
review_title[:]=[r.strip('\n') for r in review_title]
review_title

# Extract Job Description

reviews2 = soup.find_all('div', {'class': 'underShelfFooter'})
review_data2=[]    
for i in range(0,len(reviews2)):
    review_data2.append(reviews2[i].get_text())
review_data2
review_data2[:]=[d.strip('\n') for d in review_data2]
len(review_data2)
review_data2

reviews3 = soup.find_all('span', {'class': 'css-63koeb eu4oa1w0'})
review_data3=[]    
for i in range(0,len(reviews3)):
    review_data3.append(reviews3[i].get_text())
review_data3
review_data3[:]=[d.strip('\n') for d in review_data3]
len(review_data3)


###############################################################################
###############################################################################


# Assuming 'df' is your DataFrame and 'ReviewerNames' is the column containing names

len(review_title)
len(review_data2)
review_data3
# Saving the Extracted data in the csv file
import pandas as pd
df = pd.DataFrame()
df['Companies']=review_data3     # Companies Name
df['Fields']=review_title  # Job Fields
df['Job Description']=review_data2   # Job Description

df
#print(df)
###############################################################################
#Creating the csv file
#df.to_csv("I:/My Drive/study/Final Year/Final_year_Project/Dataset/_Indeed_Data_science_Fields.csv")

# Append the new DataFrame to the existing CSV file
df.to_csv("I:/My Drive/study/Final Year/Final_year_Project/Dataset/_Indeed_Data_science_Fields.csv", mode='a', index=False, header=False)

driver.quit()




