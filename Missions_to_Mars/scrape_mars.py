
import os
from bs4 import BeautifulSoup
import requests
from splinter import Browser



executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome',executable_path, headless=False)

def scrape_info():


url= 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
browser.visit(url)




html = browser.html
soup = BeautifulSoup(html, 'html.parser')





results = soup.find_all('ul', class_='item_list')
print(results)

for result in results:
    title = result.find('div', class_='content_title').text
    teaser = result.find('div', class_='article_teaser_body').text
    
    print(title)
    print('-------')
    print(teaser)




featured_image_url= "https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA18280_ip.jpg"
browser.visit(featured_image_url)


tw ='https://twitter.com/marswxreport?lang=en'
browser.visit(tw)




htmlTW = browser.html
soup = BeautifulSoup(htmlTW, 'html.parser')





print(soup.prettify())






mars_weather = soup.find_all('div',class_="css-901oao r-hkyrab r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-bnwqim r-qvutc0")
print(mars_weather)




Insight=[]

for t in mars_weather:
    if(t.span):
        if (t.span.text.startswith('InSight')):
                Insight.append(t)
                print(t)
                
            



for t in range(1):
    print(Insight[t].text)



import pandas as pd



url ='https://space-facts.com/mars/'



tables = pd.read_html(url,index_col=None)
tables



type (tables)




df = tables[0]
df.columns= ['Mars','Information']
df



df.set_index(['Mars'])




df.to_html('marstable.html')



url ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


browser.quit()