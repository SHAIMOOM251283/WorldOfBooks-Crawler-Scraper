import crawler

class SelectCategory:

    def __init__(self):
        self.home_page_url = "https://www.wob.com/en-gb/category/"
        self.category_instance = crawler.Category()  # Get category instance
        self.category_links = self.category_instance.get_category_links()  # Fetch links
        crawler.Crawler(self.category_links).run()  # Run crawler
        
    def select_category(self):
        selector = input("\nEnter the category: ")  
        self.category = selector
        search_category = self.home_page_url + selector
        print(f"\nSearch Category: {search_category}")
        return search_category
    
    def run(self):
        return self.select_category(), self.category

if __name__ == '__main__':
    select_instance = SelectCategory()
    select_instance.run()
