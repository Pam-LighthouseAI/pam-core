import requests
from bs4 import BeautifulSoup
import csv
import time
import random
import re
import sys
import os
from typing import List, Dict, Optional
import json

class AmazonScraper:
    def __init__(self, use_proxies: bool = True):
        self.base_url = "https://www.amazon.ca"
        self.search_term = "stuffed animals"
        self.products: List[Dict] = []
        self.use_proxies = use_proxies
        
        # Realistic browser headers
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Cache-Control': 'max-age=0',
        }
        
        # Common referers
        self.referers = [
            'https://www.google.com/',
            'https://www.bing.com/',
            'https://www.amazon.ca/',
            'https://www.duckduckgo.com/'
        ]
        
        # Free proxy list (will need to be updated regularly)
        self.proxies = [
            # These are example proxies - in production you'd use a real proxy service
            # "http://proxy1:port",
            # "http://proxy2:port",
        ]
        
    def get_random_header(self) -> Dict:
        """Return headers with random variations"""
        headers = self.headers.copy()
        
        # Randomize User-Agent slightly
        chrome_versions = ['120.0.0.0', '121.0.0.0', '122.0.0.0', '123.0.0.0']
        headers['User-Agent'] = f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.choice(chrome_versions)} Safari/537.36'
        
        # Add random referer
        headers['Referer'] = random.choice(self.referers)
        
        return headers
    
    def delay(self, min_seconds: float = 2.0, max_seconds: float = 5.0):
        """Random delay between requests"""
        time.sleep(random.uniform(min_seconds, max_seconds))
    
    def extract_product_data(self, product_div) -> Optional[Dict]:
        """Extract product data from a product div"""
        try:
            # Get ASIN
            asin = product_div.get('data-asin', '')
            if not asin:
                return None
            
            # Get title
            title_elem = product_div.find('span', {'class': 'a-text-normal'})
            if not title_elem:
                title_elem = product_div.find('h2', {'class': 'a-size-mini'})
            if not title_elem:
                return None
            
            title = title_elem.get_text(strip=True)
            
            # Get price
            price = ""
            price_whole = product_div.find('span', {'class': 'a-price-whole'})
            price_fraction = product_div.find('span', {'class': 'a-price-fraction'})
            
            if price_whole:
                price = price_whole.get_text(strip=True).replace(',', '')
                if price_fraction:
                    price += "." + price_fraction.get_text(strip=True)
            
            # Get rating
            rating = ""
            rating_elem = product_div.find('span', {'class': 'a-icon-alt'})
            if rating_elem:
                rating_text = rating_elem.get_text(strip=True)
                rating_match = re.search(r'(\d\.\d)', rating_text)
                if rating_match:
                    rating = rating_match.group(1)
            
            # Get review count
            review_count = ""
            reviews_elem = product_div.find('span', {'class': 'a-size-base'})
            if reviews_elem:
                review_text = reviews_elem.get_text(strip=True)
                count_match = re.search(r'([\d,]+)', review_text)
                if count_match:
                    review_count = count_match.group(1).replace(',', '')
            
            # Get link
            link = ""
            link_elem = product_div.find('a', {'class': 'a-link-normal'})
            if link_elem and link_elem.get('href'):
                link = self.base_url + link_elem['href']
            elif asin:
                link = f"{self.base_url}/dp/{asin}"
            
            # Get image URL
            image_url = ""
            img_elem = product_div.find('img', {'class': 's-image'})
            if img_elem and img_elem.get('src'):
                image_url = img_elem['src']
            
            return {
                'Title': title,
                'Price': price,
                'Rating': rating,
                'ReviewCount': review_count,
                'ASIN': asin,
                'Link': link,
                'ImageURL': image_url
            }
            
        except Exception as e:
            print(f"Error extracting product data: {e}")
            return None
    
    def scrape_page(self, page_num: int) -> List[Dict]:
        """Scrape a single page of search results"""
        url = f"{self.base_url}/s"
        params = {
            'k': self.search_term,
            'page': page_num,
            'ref': f'sr_pg_{page_num}'
        }
        
        print(f"Scraping page {page_num}...")
        
        try:
            headers = self.get_random_header()
            
            if self.use_proxies and self.proxies:
                proxy = random.choice(self.proxies)
                proxies = {'http': proxy, 'https': proxy}
                print(f"Using proxy: {proxy}")
                response = requests.get(url, params=params, headers=headers, 
                                      proxies=proxies, timeout=15)
            else:
                response = requests.get(url, params=params, headers=headers, timeout=15)
            
            response.raise_for_status()
            
            # Check for captcha or blocked page
            if "captcha" in response.text.lower() or "robot" in response.text.lower():
                print("WARNING: Possible captcha detected!")
                return []
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all product divs
            product_divs = soup.find_all('div', {'data-component-type': 's-search-result'})
            
            if not product_divs:
                # Try alternative selector
                product_divs = soup.find_all('div', {'data-asin': True})
                product_divs = [div for div in product_divs if div.get('data-asin')]
            
            print(f"Found {len(product_divs)} product containers")
            
            products = []
            for div in product_divs:
                product_data = self.extract_product_data(div)
                if product_data:
                    products.append(product_data)
            
            return products
            
        except requests.exceptions.RequestException as e:
            print(f"Request error on page {page_num}: {e}")
            return []
        except Exception as e:
            print(f"Error scraping page {page_num}: {e}")
            return []
    
    def scrape_multiple_pages(self, target_count: int = 500) -> List[Dict]:
        """Scrape multiple pages until target count is reached"""
        page_num = 1
        max_pages = 50  # Safety limit
        
        while len(self.products) < target_count and page_num <= max_pages:
            self.delay()
            
            page_products = self.scrape_page(page_num)
            
            if not page_products:
                print(f"No products found on page {page_num}. Stopping.")
                break
            
            self.products.extend(page_products)
            print(f"Page {page_num}: Got {len(page_products)} products. Total: {len(self.products)}")
            
            # Check if we're getting duplicate products
            if page_num > 1 and len(page_products) < 10:
                print("Very few products found, might be at end of results.")
                break
            
            page_num += 1
        
        # Remove duplicates by ASIN
        unique_products = []
        seen_asins = set()
        for product in self.products:
            if product['ASIN'] and product['ASIN'] not in seen_asins:
                unique_products.append(product)
                seen_asins.add(product['ASIN'])
        
        self.products = unique_products[:target_count]
        return self.products
    
    def save_to_csv(self, filename: str = "stuffed_animals_500.csv"):
        """Save products to CSV file"""
        csv_path = f"C:\\nanobot\\instance3\\workspace\\{filename}"
        
        if not self.products:
            print("No products to save!")
            return None
        
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['Title', 'Price', 'Rating', 'ReviewCount', 'ASIN', 'Link', 'ImageURL']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.products)
        
        print(f"Saved {len(self.products)} products to {csv_path}")
        return csv_path
    
    def show_sample(self, count: int = 5):
        """Show sample of scraped products"""
        if not self.products:
            print("No products scraped yet.")
            return
        
        print(f"\nSample of first {min(count, len(self.products))} products:")
        for i, product in enumerate(self.products[:count]):
            print(f"{i+1}. {product['Title'][:80]}...")
            print(f"   Price: ${product['Price']} | Rating: {product['Rating']} | Reviews: {product['ReviewCount']}")
            print(f"   ASIN: {product['ASIN']}")
            print()

def main():
    print("Amazon.ca Stuffed Animals Scraper")
    print("=" * 50)
    
    scraper = AmazonScraper(use_proxies=False)  # Start without proxies
    
    print(f"Target: 500 products")
    print(f"Search term: 'stuffed animals'")
    print(f"Base URL: {scraper.base_url}")
    print()
    
    # Scrape products
    products = scraper.scrape_multiple_pages(target_count=500)
    
    if not products:
        print("Failed to scrape any products. Trying alternative approach...")
        # Try with different headers or approach
        return
    
    # Save to CSV
    csv_file = scraper.save_to_csv()
    
    # Show summary
    print("\n" + "=" * 50)
    print("SCRAPING COMPLETE")
    print(f"Total products scraped: {len(products)}")
    print(f"CSV file: {csv_file}")
    print("=" * 50)
    
    # Show sample
    scraper.show_sample(5)
    
    return csv_file, len(products)

if __name__ == "__main__":
    csv_file, count = main()