
class Book:
    id :int
    title :str
    author :str
    category :str
    description :str

    def __init__(self,id,title,author,category,description):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.description=description