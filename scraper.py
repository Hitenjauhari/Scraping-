import requests
from bs4 import BeautifulSoup
import json
import pandas as pd

df = pd.read_csv('amazon-urls-data.csv')

results = []

# Visit Url and provide result
def scrape_url(country, asin):
    url = f"https://www.amazon.{country}/dp/{asin}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            results.append({
                'Api': url,
                'Status': 'success',
                'Status Code': response.status_code,
                'data': {
                    'Product Title': title,
                    'Product Image URL': image_url,
                    'Price of the Product': price,
                    'Product Details': product_details
                }
            })
        else:
            print(f"Error: {url} returned status code {response.status_code}")
            results.append({
                'Api': url,
                'Status': 'failure',
                'Status Code': response.status_code,
                'data': {}
            })
    except Exception as e:
        print(f"Error: {e}")


# for each loop getting a calling api
for index, row in df.iterrows():
    scrape_url(row['country'], row['Asin'])

# dumping data to output file
with open('output.json', 'w') as json_file:
    json.dump(results, json_file)

print("Scraping amazon data successfully.")
