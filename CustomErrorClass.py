class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.page_read = 0


    def __repr__(self):
        return(f"Book{self.name},read {self.page_read} pages out of {self.page_count}")


    def read(self, pages: int):
        if self.page_read + pages > self.page_count:
            raise ValueError(f"You tried to read {self.page_read + pages} pages but this book only has {self.page_count} pages")
        
        self.page_read += pages
        print(f"You have now read {self.page_read} pages out of {self.page_count}.")


python = Book("Python 101",50)

try:
    python.read(50)
    python.read(50)
except ValueError as e:
    print(e)