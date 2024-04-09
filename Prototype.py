import copy


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def clone(self):
        return copy.deepcopy(self)


prototype_book = Book("Martin Eden", "Jack London", 500)

clone_book = prototype_book.clone()

print("Clone Book Details:")
print(clone_book)
