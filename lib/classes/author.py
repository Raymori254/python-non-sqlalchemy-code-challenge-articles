class Author:
    all = []

    def _init_(self, name):
        self._name = None
        self.name = name  
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if self._name is not None:
           return
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magazine = {article.magazine for article in self.articles()}
        return list(magazine) if magazine else None

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        categories = {article.magazine.category for article in self.articles()}
        return list(categories)