class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self._title = None
        self.title = title
        self.author = author
        self.magazine = magazine
        author._articles.append(self)
        magazine._articles.append(self)
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, '_title') and self._title is not None:
            raise AttributeError("Title cannot be changed")
        if not isinstance(title, str) or not 5 <= len(title) <= 50:
            raise ValueError("Title must be 5-50 chars")
        self._title = title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise ValueError("Author must be Author type")
        self._author = author
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be Magazine type")
        self._magazine = magazine


class Author:
    def __init__(self, name):
        self._name = None
        self.name = name
        self._articles = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if self._name is not None:
            raise AttributeError("Name cannot be changed")
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be non-empty string")
        self._name = name
    
    def articles(self):
        return self._articles
    
    def magazines(self):
        return list({article.magazine for article in self._articles})
    
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        return article
    
    def topic_areas(self):
        if not self._articles:
            return None
        return list({magazine.category for magazine in self.magazines()})


class Magazine:
    all = []
    
    def __init__(self, name, category):
        self._name = None
        self._category = None
        self.name = name
        self.category = category
        self._articles = []
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str) or not 2 <= len(name) <= 16:
            raise ValueError("Name must be 2-16 chars")
        self._name = name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be non-empty")
        self._category = category
    
    def articles(self):
        return self._articles
    
    def contributors(self):
        return list({article.author for article in self._articles})
    
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
    
    def contributing_authors(self):
        counts = {}
        for article in self._articles:
            counts[article.author] = counts.get(article.author, 0) + 1
        result = [a for a, c in counts.items() if c > 2]
        return result if result else None
    
    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda m: len(m.articles()), default=None)