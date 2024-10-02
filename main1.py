import requests
from bs4 import BeautifulSoup
import json  # Import json module

class ArticleExtractor:
    def __init__(self, url):
        self.url = url

    def fetch_html(self):
        try:
            response = requests.get(self.url, headers={'User-Agent': 'Custom User Agent'})
            if response.status_code == 200:
                return response.text
            else:
                print(f"Failed to fetch the webpage. Status Code: {response.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error fetching the webpage: {e}")
            return None

    def parse_articles(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        # Placeholder for the correct CSS selectors based on the website’s structure
        articles = soup.find_all('div', class_='article-class')  # Example selector, adjust as needed
        articles_list = []
        for article in articles:
            title = article.find('h2').text.strip()  # Assuming titles are in <h2>
            link = article.find('a')['href'].strip()  # Assuming the article links are in <a> tags within the article div
            articles_list.append({"Title": title, "Link": link})
        
        return articles_list

    def save_to_json(self, articles, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(articles, file, ensure_ascii=False, indent=4)
    
    def run(self):
        html = self.fetch_html()
        if html:
            articles_list = self.parse_articles(html)
            if articles_list:
                self.save_to_json(articles_list, 'articles.json')
                print(f"Saved {len(articles_list)} articles to articles.json")

if __name__ == "__main__":
    url = 'https://www.nytimes.com/'  # Adjust the website's URL as needed
    scraper = ArticleExtractor(url)
    scraper.run()