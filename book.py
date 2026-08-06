class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def display(self):
        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)