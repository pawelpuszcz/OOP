class Book:
    language = 'ENG'
    is_ebook = True

    def set_title(self, value):
        self.title = value

book = Book()

book.set_title('Inferno')

print(book.title)
