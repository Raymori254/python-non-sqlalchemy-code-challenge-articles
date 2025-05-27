class Magazine:
    all = []

    def _init_(self, name, category):
        self._name = None
        self._category = None
        self.name = name  # Uses the name setter
        self.category = category  # Uses the category setter
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            return
        if len(value) < 2 or len(value) > 16:
            return
        self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            return
        if len(value) == 0:
            return
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = {article.author for article in self.articles()}
        return list(authors) if authors else None

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        authors = [article.author for article in self.articles()]
        counts = {author: authors.count(author) for author in set(authors)}
        result = [author for author, count in counts.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))