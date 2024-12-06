import requests
from scrappers.mat.classes.scrapper import Scrapper as MatScrapper
from scrappers.news.classes.scrapper import Scrapper as NewsScrapper

IS_DEV = False

API_URL = "http://localhost:8000" if IS_DEV else "https://api-tas.gadsw.dev"


def insert_news(title: str, content: str, news_url: str):
    url = f"{API_URL}/data-element/create-data/"
    data = {"title": title, "content": content, "url": news_url, "type": "news"}
    headers = {"Accept": "application/json", "Content-Type": "application/json"}
    request = requests.post(url, json=data, headers=headers)
    if request.status_code != 200:
        print(f"ERROR inserting news: {url}")
    print(f"Saved news {title}")


def insert_mat_results(results: list):
    for result in results:
        url = f"{API_URL}/data-element/create-data/"
        data = {
            "title": result["name"],
            "content": result["description"],
            "url": result["url"],
            "type": "mat",
        }
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        request = requests.post(url, json=data, headers=headers)
        if request.status_code != 200:
            print(f"ERROR inserting news: {url}")
        print(f"Saved mat  {result['name']}")


def main():
    news_scrapper = NewsScrapper()
    mat_scrapper = MatScrapper()
    news_data = news_scrapper.get_all_news()
    mat_scrapper.get_results()
    insert_mat_results(mat_scrapper.results)
    for _, row in news_data.iterrows():
        title = row["title"]
        content = row["content"]
        url = row["url"]
        insert_news(title, content, url)


if __name__ == "__main__":
    main()
