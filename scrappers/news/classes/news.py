

class News:
    def __init__(self, title: str, url: str, content: str) -> None:
        self.title = self.remove_spaces_from_title(title)
        self.url = url
        self.content = content


    def __str__(self) -> str:
        return f"{self.title} - {self.url} - \n{self.content}"


    def remove_spaces_from_title(self, title: str) -> str:
        trash_characters = [
            "\n",
            "\r",
            "\t",
        ]
        letters = [letter for letter in title if (letter not in trash_characters)]
        return "".join(letters).strip()
    
    def to_dict(self):
        return {
            "title": self.title,
            "url": self.url,
            "content": self.content
        }