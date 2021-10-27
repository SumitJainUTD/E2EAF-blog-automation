class Post:
    def __init__(self, title=None, content=None, slug=None, author=None):
        self.title = title
        self.content = content
        self.author = author
        self.slug = slug