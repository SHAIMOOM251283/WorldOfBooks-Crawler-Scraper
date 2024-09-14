import crawler

class SelectCategory:

    def __init__(self):
        self.home_page_url = "https://www.wob.com/en-gb/category/"
        self.crawler = crawler.WebCrawler() 
        self.crawler.run()

    def select_category(self):
        selector = input("\nEnter keyword (e.g. crime-mystery): ")  
        self.category = selector
        search_category = self.home_page_url + selector
        print(f"\nSearch Category: {search_category}")
        return search_category
    
    def run(self):
        return self.select_category(), self.category

if __name__ == '__main__':
    select_instance = SelectCategory()
    select_instance.run()
