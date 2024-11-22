from scrappers.news.scrapper import Scrapper as NewsScrapper


def main():
    news_scrapper = NewsScrapper()
    news_data = news_scrapper.get_all_news()
    print(f"Columns: {news_data.columns}")

if __name__ == "__main__":
    main()
