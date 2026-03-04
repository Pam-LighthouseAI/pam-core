import requests
from bs4 import BeautifulSoup
import csv
import time
import random
import re

def scrape_amazon_fast():
    """Fast scraper for Amazon.ca stuffed animals"""
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }
    
    base_url = "https://www.amazon.ca"
    products = []
    page = 1
    max_pages = 20  # Limit pages to avoid timeout
    target_count = 500
    
    csv_file = "C:\\nanobot\\instance3\\workspace\\stuffed_animals_500.csv"
    
    print("Starting Amazon.ca scrape for stuffed animals...")
    
    while len(products) < target_count and page <= max_pages:
        try:
            # Construct search URL
            url = f"{base_url}/s"
            params = {
                'k': 'stuffed animals',
                'page': page,
                'crid': '2QN6J54G5ZQ18',
                'sprefix': 'stuffed+animals%2Caps%2C92',
                'ref': f'sr_pg_{page}'
            }
            
            # Add delay
            time.sleep(random.uniform(1, 3))
            
            response = requests.get(url, params=params, headers=headers, timeout=15)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Look for product containers
            items = soup.find_all('div', {'data-component-type': 's-search-result'})
            
            if not items:
                # Try alternative selector
                items = soup.find_all('div', {'data-asin': True})
                items = [item for item in items if item.get('data-asin') and item.get('data-asin') != '']
            
            print(f"Page {page}: Found {len(items)} items")
            
            for item in items:
                if len(products) >= target_count:
                    break
                    
                try:
                    # Extract data
                    asin = item.get('data-asin', '')
                    
                    # Title
                    title_elem = item.find('span', class_='a-text-normal')
                    if not title_elem:
                        title_elem = item.find('h2', class_='a-size-mini')
                    title = title_elem.get_text(strip=True) if title_elem else "No title"
                    
                    # Price
                    price_whole = item.find('span', class_='a-price-whole')
                    price_fraction = item.find('span', class_='a-price-fraction')
                    price = ""
                    if price_whole:
                        price = price_whole.get_text(strip=True).replace(',', '')
                        if price_fraction:
                            price += "." + price_fraction.get_text(strip=True)
                    
                    # Rating
                    rating_elem = item.find('span', class_='a-icon-alt')
                    rating = ""
                    if rating_elem:
                        rating_text = rating_elem.get_text(strip=True)
                        rating_match = re.search(r'(\d\.\d)', rating_text)
                        if rating_match:
                            rating = rating_match.group(1)
                    
                    # Review count
                    reviews_elem = item.find('span', class_='a-size-base')
                    review_count = ""
                    if reviews_elem:
                        review_text = reviews_elem.get_text(strip=True)
                        count_match = re.search(r'([\d,]+)', review_text)
                        if count_match:
                            review_count = count_match.group(1).replace(',', '')
                    
                    # Link
                    link_elem = item.find('a', class_='a-link-normal')
                    link = ""
                    if link_elem and link_elem.get('href'):
                        link = base_url + link_elem['href']
                    elif asin:
                        link = f"{base_url}/dp/{asin}"
                    
                    # Image
                    img_elem = item.find('img', class_='s-image')
                    image_url = img_elem['src'] if img_elem and img_elem.get('src') else ""
                    
                    # Add product if we have basic info
                    if title != "No title" and asin:
                        product = {
                            'Title': title,
                            'Price': price,
                            'Rating': rating,
                            'ReviewCount': review_count,
                            'ASIN': asin,
                            'Link': link,
                            'ImageURL': image_url
                        }
                        products.append(product)
                        
                        if len(products) % 50 == 0:
                            print(f"  Collected {len(products)} products so far...")
                            
                except Exception as e:
                    continue
            
            page += 1
            
        except Exception as e:
            print(f"Error on page {page}: {e}")
            break
    
    # Save to CSV
    print(f"\nSaving {len(products)} products to CSV...")
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['Title', 'Price', 'Rating', 'ReviewCount', 'ASIN', 'Link', 'ImageURL']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)
    
    return csv_file, len(products)

if __name__ == "__main__":
    csv_path, count = scrape_amazon_fast()
    print(f"\nScraping complete!")
    print(f"Total products: {count}")
    print(f"File saved to: {csv_path}")
    
    # Show sample
    if count > 0:
        print("\nSample products:")
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            sample = []
            for i, row in enumerate(reader):
                if i < 5:
                    sample.append(row)
        
        for i, product in enumerate(sample):
            print(f"{i+1}. {product['Title'][:70]}...")
            print(f"   Price: ${product['Price']} | Rating: {product['Rating']} | Reviews: {product['ReviewCount']}")
            print()