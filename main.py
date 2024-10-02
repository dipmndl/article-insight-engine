import sys
import os
from src.feed_finder_2 import FeedFinder2
from src.article_extractor import ArticleExtractor
from src.article_processor import ArticleProcessor
import json
from loguru import logger

EXTRACT_ARTICLES = True
TRANSLATE_LANGUAGE = "english"

def main():
    # Load config
    with open(os.environ["SITES_LIST_FILE"], encoding='utf-8') as sites_list_file:
        sites_list = json.load(sites_list_file)

    # Initialize classes
    #article_processor = ArticleProcessor()

    # Prepare the results dictionary
    results = []

    # Process each website
    for site in sites_list:
        logger.info(f"Processing site: {site['URL']}")
        site_data = {
            "site_url": site['URL'],
            "feeds": []
        }

        rss_url = site.get("RSS_URL")
        if not rss_url:
            # Find feed V2
            finder = FeedFinder2(site['URL'])
            rss_links = finder.find_feed()

            if EXTRACT_ARTICLES is True:
                if rss_links:
                    for rss_link in rss_links:
                        extractor = ArticleExtractor()
                        articles = extractor.extract_articles(rss_link)
                        feed_data = {
                            "rss_url": rss_link,
                            "articles": []
                        }

                        for article in articles[:10]:  # Take only the first 10 articles
                            logger.info(f"Processing article: {article['title']}")
                            
                            article_categories = os.environ["ARTICLE_CATEGORIES"].split(",")
                            ''' 
                            article_data = {
                                "link": article['link'],
                                "title": article_processor.translate(article["title"], TRANSLATE_LANGUAGE),
                                "language": article_processor.detect_language(article["summary"]),
                                "text": "",
                                "summary": article_processor.translate(article["summary"], TRANSLATE_LANGUAGE),
                                "category": article_processor.categorize_article(article["summary"], article_categories),
                                "timestamp": ""
                            }
                            '''
                            article_data = {
                                "link": '',
                                "title": '',
                                "language": '',
                                "text": "",
                                "summary": '',
                                "category": '',
                                "timestamp": ""
                            }
                            feed_data["articles"].append(article_data)

                        site_data["feeds"].append(feed_data)
                else:
                    # No RSS feeds found, extract articles directly from HTML
                    articles = finder.extract_articles_from_html()
                    feed_data = {
                        "feed_url": None,
                        "articles": articles
                    }
                    site_data["feeds"].append(feed_data)

        # Append site data to results
        results.append(site_data)

    # Output the results as JSON
    with open('results.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    # Collect statistics

if __name__ == "__main__":
    main()