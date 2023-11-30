from bs4 import BeautifulSoup
import requests
import csv

# source
base_url = 'https://www.property24.com/for-sale/somerset-west/western-cape/390/p'

#number of pages
num_pages = 5

# open csv file for writing
with open('data.csv', 'w', encoding='utf8', newline='') as f:
    writer = csv.writer(f)
    header = ['Title','Price','Location','Bedrooms','Bathrooms','Parking','Size','Description']
    writer.writerow(header)

    # loop over each page and scrape data
    for page_num in range(1, num_pages + 1):
        # construct page URL
        url = base_url + str(page_num)
        

        # retrieve page content
        page = requests.get(url)
        print("Downloading Page number:",page_num)
        
        soup = BeautifulSoup(page.content, 'html.parser')
        print("Page number",page_num,"download complete")

        # find all relevant elements
        properties = soup.find_all('span', class_='p24_content')
        print(len(properties),"properties found for page", page_num)
        
        print("")

        # loop over each element and extract data
        for prop in properties:
            title = prop.find('span', class_='p24_title').text.replace('\n', '')
            price = prop.find('span', class_='p24_price').text.replace('\n', '').replace('\r', '')
            
            #Area
            location = prop.find('span', class_='p24_location').text.replace('\n', '').replace('\r', '')
            
            #bedrooms
            try:
                beds = prop.find('span',class_='p24_featureDetails',title='Bedrooms').text.replace('\n', '')
            except:
                beds = 0
                
            #bathrooms
            try:
                bathrooms = prop.find('span',class_='p24_featureDetails',title='Bathrooms').text.replace('\n', '')
            except:
                bathrooms = 0
                
            #get parking
            try:
                parking = prop.find('span',class_='p24_featureDetails',title='Parking Spaces').text.replace('\n', '')
            except:
                parking = 0
                
            #get size
            try
                size = lists[0].find('span',class_='p24_size').text.replace('\n', '')
            except:
                size = 0
                
            #description
            description = prop.find('span', class_='p24_excerpt').text.replace('\n', '').replace('\r', '')
            
            #Write to file
            info = [title,price,location,beds,bathrooms,parking,size,description]
            writer.writerow(info)

print('Scraping complete!')