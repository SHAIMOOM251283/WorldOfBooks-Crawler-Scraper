import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class Category:
    def __init__(self):
        self.home_page_url = "https://www.wob.com/en-gb"
        self.response = requests.get(self.home_page_url)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

    def get_category_links(self):
        category_links = {}
        categories = self.soup.find_all('div', class_='categoryItem')
    
        for category in categories:
            link_tag = category.find('a', class_='categoryName')
            if link_tag:
                category_name = link_tag.text.strip().upper()
                category_url = urljoin(self.home_page_url, link_tag['href'])
                category_links[category_name] = category_url
        
        for name, url in category_links.items():
            print(f"{name}: {url}")
        
        return category_links

class Crawler:
    def __init__(self, category_links):
        self.urls = category_links

    def scrape_category(self, category_name, url):
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            category_div = soup.find('div', class_='categoryFilter')
            category_links = category_div.find_all('a')

            print(f"\t\t\t\t\t***{category_name}***")
            for link in category_links:
                subcategory_name = link.text.strip()
                subcategory_url = urljoin(url, link['href'])
                print(f'Category: {subcategory_name}')
                print(f'URL: {subcategory_url}')
                print('-' * 40)
        else:
            print(f"Failed to retrieve the page for {category_name}. Status code: {response.status_code}")

    def run(self):
        for category_name, url in self.urls.items():
            self.scrape_category(category_name, url)

if __name__ == '__main__':
    # First, get the category URLs
    category_fetcher = Category()
    category_links = category_fetcher.get_category_links()

    # Then, scrape each category
    crawler = Crawler(category_links)
    crawler.run()
