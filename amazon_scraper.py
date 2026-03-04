import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

base_url = 'https://www.amazon.ca/s?k=stuffed+animals&amp;page={}'
data = []
page = 1
max_pages = 50  # safety

print('Starting scrape...')

while len(data) < 200 and page <= max_pages:
    url = base_url.format(page)
    print(f'Fetching page {page}: {url}')
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f'Failed to fetch page {page}: {response.status_code}')
            break
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find product containers
        products = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        if not products:
            print('No products found on page', page)
            break
        
        page_items = 0
        for prod in products:
            if len(data) >= 200:
                break
            
            # Skip sponsored if wanted, but include for now
            if 'Sponsored' in prod.text:
                continue
                
            asin = prod.get('data-asin', '')
            if not asin:
                continue
            
            # Title
            title_elem = prod.find('h2')
            title = ''
            if title_elem:
                spans = title_elem.find_all('span')
                if spans:
                    title = spans[0].get_text(strip=True)
            
            # Link
            link_elem = prod.find('a', {'class': 'a-link-normal'})
            link = ''
            if link_elem:
                href = link_elem.get('href', '')
                if href.startswith('/'):
                    link = 'https://www.amazon.ca' + href
                else:
                    link = href
            
            # Price
            price = ''
            price_whole = prod.find('span', {'class': 'a-price-whole'})
            if price_whole:
                price = price_whole.get_text(strip=True)
            else:
                price_frac = prod.find('span', {'class': 'a-price-fraction'})
                if price_frac:
                    price = price_frac.get_text(strip=True)
            
            # Rating
            rating_elem = prod.find('span', {'class': 'a-icon-alt'})
            rating = ''
            if rating_elem:
                rating_text = rating_elem.get_text(strip=True)
                # Extract stars, e.g. "4.5 out of 5 stars"
                match = re.search(r'(\d+\.?\d*) out of 5', rating_text)
                if match:
                    rating = match.group(1)
            
            # Review count
            review_count_elem = prod.find('span', {'class': 'a-size-base'})
            review_count = ''
            if review_count_elem:
                review_text = review_count_elem.get_text(strip=True)
                # Extract number, e.g. "(1,234)"
                match = re.search(r'\((\d+(?:,\d{3})*)\)', review_text)
                if match:
                    review_count = match.group(1)
            
            # Image
            img_elem = prod.find('img', {'class': 's-image'})
            img_url = ''
            if img_elem:
                img_url = img_elem.get('src', img_elem.get('data-a-dynamic-image', ''))
                if 'data-a-dynamic-image' in img_elem.attrs:
                    # Take first
                    img_url = list(img_elem['data-a-dynamic-image'].keys())[0] if img_elem['data-a-dynamic-image'] else ''
            
            if title:  # Only add if title
                data.append({
                    'Title': title,
                    'Price': price,
                    'Rating': rating,
                    'ReviewCount': review_count,
                    'ASIN': asin,
                    'Link': link,
                    'ImageURL': img_url
                })
                page_items += 1
        
        print(f'Page {page}: extracted {page_items} items, total {len(data)}')
        
    except Exception as e:
        print(f'Error on page {page}: {str(e)}')
        break
    
    page += 1
    if page > 1:
        time.sleep(5)  # Delay between pages

# Save to CSV
if data:
    df = pd.DataFrame(data)
    csv_path = r'C:\nanobot\instance3\workspace\stuffed_animals.csv'
    df.to_csv(csv_path, index=False)
    print(f'Saved {len(data)} rows to {csv_path}')
    print('\\nSample rows:')
    print(df.head(5).to_csv(index=False))
else:
    print('No data scraped')