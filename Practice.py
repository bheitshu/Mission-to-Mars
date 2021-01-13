#!/usr/bin/env python
# coding: utf-8

# In[9]:


from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[10]:


ChromeDriverManager().install()


# In[11]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[12]:


# Visit the Quotes to Scrape site
url = 'http://quotes.toscrape.com/'
browser.visit(url)


# In[13]:


# Parse the HTML
html = browser.html
html_soup = soup(html, 'html.parser')


# In[14]:


# Scrape the Title
title = html_soup.find('h2').text
title


# In[15]:


# Scrape the top ten tags
tag_box = html_soup.find('div', class_='tags-box')
# tag_box
tags = tag_box.find_all('a', class_='tag')

for tag in tags:
    word = tag.text
    print(word)


# In[16]:


url = 'http://quotes.toscrape.com/'
browser.visit(url)


# In[17]:


for x in range(1, 6):
   html = browser.html
   quote_soup = soup (html, 'html.parser')
   quotes = quote_soup.find_all('span', class_='text')
   for quote in quotes:
      print('page:', x, '----------')
      print(quote.text)
   browser.links.find_by_partial_text('Next')


# In[18]:


browser.quit()


# In[23]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup


# In[24]:


ChromeDriverManager().install()


# In[26]:


# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': '/Users/brookeheitshu/.wdm/drivers/chromedriver/mac64/87.0.4280.88/chromedriver'}
browser = Browser('chrome', **executable_path)


# In[27]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[28]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')


# In[29]:


slide_elem.find("div", class_='content_title')


# In[30]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[31]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### Featured Images

# In[32]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[33]:


# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()


# In[34]:


# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()


# In[35]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[36]:


# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel


# In[37]:


# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url


# In[39]:


import pandas as pd


# In[40]:


df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df


# In[42]:


df.to_html()


# In[43]:


browser.quit()


# In[ ]:




