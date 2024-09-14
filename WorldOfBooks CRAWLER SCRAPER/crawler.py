import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class WebCrawler:
    def __init__(self):
        self.home_page_url = "https://www.wob.com/en-gb"
        self.response = requests.get(self.home_page_url)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')
        
    # Step 1: Extract main category links
    def crawl_homepage(self):
        main_links = {}
        link_containers = self.soup.find_all('div', class_='categoryItem')

        for container in link_containers:
            link_tag = container.find('a', class_='categoryName')
            if link_tag:
                name = link_tag.text.strip().upper()
                link_url = urljoin(self.home_page_url, link_tag['href'])
                main_links[name] = link_url
        
        # Print each category and its URL
        for name, url in main_links.items():
            print(f"{name}: {url}")
        
        return main_links

    # Step 2: Scrape details from each category
    def extract_urls(self):
        main_links = self.crawl_homepage()  # Fetch category links inside this method
        
        for category_name, url in main_links.items():
            print(f"\nScraping: {category_name} - {url}")
            response = requests.get(url)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # Add logic to scrape more details from the category page
                category_div = soup.find('div', class_='categoryFilter')
                if category_div:
                    categories = category_div.find_all('a')
                    for cat in categories:
                        cat_name = cat.text.strip()
                        cat_url = urljoin(url, cat['href'])
                        print(f"  Category: {cat_name} - {cat_url}")
                else:
                    print(f"No Categories found for {category_name}")
            else:
                print(f"Failed to retrieve {category_name}. Status code: {response.status_code}")

    # Step 3: Run the crawler
    def run(self):
        self.extract_urls()  # This now handles both fetching links and scraping details

if __name__ == '__main__':
    crawler = WebCrawler()
    crawler.run()
