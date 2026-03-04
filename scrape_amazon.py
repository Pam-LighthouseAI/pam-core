import requests
from bs4 import BeautifulSoup
import time
import random
import csv
import re
import os
from urllib.parse import urljoin, urlencode

def scrape_amazon_stuffed_animals():
    """Scrape stuffed animals from Amazon.ca"""
    
    # Headers to mimic browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Connection': 'keep-alive',
    }
    
    base_url = "https://www.amazon.ca"
    search_query = "stuffed animals"
    
    # CSV setup
    csv_file = "C:\\nanobot\\instance3\\workspace\\stuffed_animals_500.csv"
    fieldnames = ['Title', 'Price', 'Rating', 'ReviewCount', 'ASIN', 'Link', 'ImageURL']
    
    products = []
    page = 1
    
    print(f"Starting scrape of Amazon.ca for '{search_query}'...")
    print(f"Target: 500 products")
    print(f"CSV will be saved to: {csv_file}")
    
    while len(products) < 500:
        # Construct search URL
        params = {
            'k': search_query,
            'page': page,
            'ref': f'sr_pg_{page}'
        }
        
        search_url = f"{base_url}/s?{urlencode(params)}"
        print(f"Scraping page {page}: {search_url}")
        
        try:
            # Add delay to be respectful
            delay = random.uniform(2, 5)
            time.sleep(delay)
            
            response = requests.get(search_url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find product containers
            # Amazon product containers typically have data-asin attribute
            product_elements = soup.find_all('div', {'data-component-type': 's-search-result'})
            
            if not product_elements:
                print("No products found on this page. Trying alternative parsing...")
                # Try alternative selectors
                product_elements = soup.find_all('div', {'data-asin': True})
                
            print(f"Found {len(product_elements)} product elements on page {page}")
            
            for product in product_elements:
                if len(products) >= 500:
                    break
                    
                try:
                    # Extract ASIN
                    asin = product.get('data-asin', '')
                    if not asin:
                        # Try to find ASIN in other attributes
                        asin_match = re.search(r'/dp/([A-Z0-9]{10})', str(product))
                        if asin_match:
                            asin = asin_match.group(1)
                    
                    # Extract title
                    title_elem = product.find('span', {'class': 'a-text-normal'})
                    if not title_elem:
                        title_elem = product.find('h2', {'class': 'a-size-mini'})
                    
                    title = title_elem.get_text(strip=True) if title_elem else "No title"
                    
                    # Extract price
                    price_elem = product.find('span', {'class': 'a-price-whole'})
                    price_fraction = product.find('span', {'class': 'a-price-fraction'})
                    
                    price = ""
                    if price_elem:
                        price = price_elem.get_text(strip=True)
                        if price_fraction:
                            price += "." + price_fraction.get_text(strip=True)
                    
                    # Extract rating
                    rating_elem = product.find('span', {'class': 'a-icon-alt'})
                    rating = ""
                    if rating_elem:
                        rating_text = rating_elem.get_text(strip=True)
                        rating_match = re.search(r'(\d\.\d)', rating_text)
                        if rating_match:
                            rating = rating_match.group(1)
                    
                    # Extract review count
                    review_elem = product.find('span', {'class': 'a-size-base'})
                    review_count = ""
                    if review_elem:
                        review_text = review_elem.get_text(strip=True)
                        # Look for numbers in review text
                        review_match = re.search(r'([\d,]+)', review_text)
                        if review_match:
                            review_count = review_match.group(1).replace(',', '')
                    
                    # Extract link
                    link_elem = product.find('a', {'class': 'a-link-normal'})
                    if link_elem and link_elem.get('href'):
                        link = urljoin(base_url, link_elem['href'])
                    else:
                        # Construct link from ASIN
                        link = f"{base_url}/dp/{asin}" if asin else ""
                    
                    # Extract image URL
                    img_elem = product.find('img', {'class': 's-image'})
                    image_url = img_elem['src'] if img_elem and img_elem.get('src') else ""
                    
                    # Only add if we have at least a title and ASIN
                    if title != "No title" and asin:
                        product_data = {
                            'Title': title,
                            'Price': price,
                            'Rating': rating,
                            'ReviewCount': review_count,
                            'ASIN': asin,
                            'Link': link,
                            'ImageURL': image_url
                        }
                        products.append(product_data)
                        print(f"  Added product {len(products)}: {title[:50]}...")
                        
                except Exception as e:
                    print(f"  Error processing product: {e}")
                    continue
            
            # Check if we should continue to next page
            if len(product_elements) == 0:
                print("No more products found. Stopping.")
                break
                
            page += 1
            
        except Exception as e:
            print(f"Error scraping page {page}: {e}")
            break
    
    # Save to CSV
    print(f"\nSaving {len(products)} products to CSV...")
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)
    
    print(f"Done! Saved {len(products)} products to {csv_file}")
    return csv_file, len(products)

if __name__ == "__main__":
    csv_path, count = scrape_amazon_stuffed_animals()
    print(f"\nSummary:")
    print(f"- Products scraped: {count}")
    print(f"- File saved: {csv_path}")
    
    # Show first few rows
    if count > 0:
        print("\nFirst 3 products:")
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                if i < 3:
                    print(f"{i+1}. {row['Title'][:60]}... | Price: {row['Price']} | Rating: {row['Rating']}")
                else:
                    break