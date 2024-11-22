import requests

import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from .classes.news import News


class Scrapper:
    def __init__(self) -> None:
        self.soup: BeautifulSoup = None
        self.main_url: str = "https://sistemas.unmsm.edu.pe"
        self.soup: BeautifulSoup | None = self.create_soup(url=self.main_url)

    def create_soup(self, url: str):
        user_agent = UserAgent()
        page = requests.get(
            url, headers={"User-Agent": user_agent.chrome}
        )
        if page.status_code == 404:
            print("ERROR creating soup")
            return None
        soup = BeautifulSoup(page.content, "html.parser")
        return soup

    def get_news_content(self, news_url: str):
        soup = self.create_soup(news_url)
        if soup is None:
            return None
        news_tittle = soup.find("h1", class_="article_title").find("a").text
        news_content = soup.find("div", class_="newsitem_text").text
        return news_tittle, news_content

    def get_info_from_main_post(self, post):
        news_url = post.find("a")["href"]
        full_url = f"{self.main_url}/{news_url}"
        news_title, news_content = self.get_news_content(news_url=full_url)
        if news_content is None:
            return None
        news = News(title=news_title, url=full_url, content=news_content)
        return news

    def get_info_from_under_post(self, post):
        news_url = post["href"]
        full_url = f"{self.main_url}/{news_url}"
        news_title, news_content = self.get_news_content(news_url=full_url)
        if news_content is None:
            return None
        news = News(title=news_title, url=full_url, content=news_content)
        return news

    def get_all_news(self):
        news_list: list[dict] = []
        under_posts = self.get_under_posts()
        main_posts = self.get_main_posts()
        for post in main_posts:
            news = self.get_info_from_main_post(post)
            if news is not None:
                news_list.append(news.to_dict())

        for post in under_posts:
            news = self.get_info_from_under_post(post)
            if news is not None:
                news_list.append(news.to_dict())

        news_df = pd.DataFrame(news_list)

        return news_df

    def get_under_posts(self):
        news_items = self.soup.find_all("div", class_="mfp_carousel_item")
        news_list = [
            item.find("h4", class_="mfp_carousel_title").find("a")
            for item in news_items
        ]
        return news_list

    def get_main_posts(self):
        if self.soup is None:
            return None
        carousel = self.soup.find("div", id="Youdeveloperslider").find(
            "div", class_="elements"
        )
        slides = carousel.find_all("div", class_="slide")
        return slides

    def get_latest_under_post(self) -> News:
        if self.soup is None:
            return None
        news_items = self.soup.find_all("div", class_="mfp_carousel_item")
        news_list = [
            item.find("h4", class_="mfp_carousel_title").find("a")
            for item in news_items
        ]
        first_post = news_list[0]
        news_url = first_post["href"]
        full_url = f"{self.main_url}/{news_url}"
        news_title, news_content = self.get_news_content(news_url=full_url)
        news = News(title=news_title, url=full_url, content=news_content)
        return news

    def get_latest_main_post(self) -> News:
        if self.soup is None:
            return None
        carousel = self.soup.find("div", id="Youdeveloperslider").find(
            "div", class_="elements"
        )
        slides = carousel.find_all("div", class_="slide")
        first_slide = slides[0].find("div", class_="title")
        news_url = first_slide.find("a")["href"]
        full_url = f"{self.main_url}/{news_url}"
        news_title, news_content = self.get_news_content(news_url=full_url)
        news = News(title=news_title, url=full_url, content=news_content)
        return news
