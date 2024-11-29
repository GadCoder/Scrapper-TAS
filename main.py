import requests
from scrappers.news.scrapper import Scrapper as NewsScrapper


IS_DEV = True

API_URL = "http://localhost:8000" if IS_DEV else "https://api-tas.gadsw.dev"


def insert_news(title: str, content: str, news_url: str):
    url = f"{API_URL}/news/create-news/"
    data = {"title": title, "content": content, "url": news_url}
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    request = requests.post(url, json=data, headers=headers)
    if request.status_code != 200:
        print(f"ERROR inserting news: {url}")
    print(f"Saved news {title}")


def main():
    news_scrapper = NewsScrapper()
    news_data = news_scrapper.get_all_news()
    for _, row in news_data.iterrows():
        title = row["title"]
        content = row["content"]
        url = row["url"]
        insert_news(title, content, url)


if __name__ == "__main__":
    main()
