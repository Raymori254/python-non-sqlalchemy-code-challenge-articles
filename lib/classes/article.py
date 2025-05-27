class Article:
    all = []  # Class variable to store all Article instances

    def _init_(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = None
        self.title = title  
        Article.all.append(self) 

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if self._title is not None:
            raise AttributeError("Title cannot be changed after instantiation")
        if not isinstance(value, str):
            raise ValueError("Title must be a string")
        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = value

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be an instance of Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        self._magazine = value