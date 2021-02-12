class Book:

    Types = ["hardcore","Paperback","E-Book"]

    def __init__(self, name,book_types, weight):
        self.name = name
        self.book_types = book_types
        self.weight = weight
        
       

    def __str__(self):
        return f"The book is {self.name}, and Types is {self.book_types}, & Weight is {self.weight}."    

    def __repr__(self):
        return f"Book {self.name},{self.book_types},{self.weight}."

    @classmethod
    def hardcore(cls,name, page_weight):
        return Book(name, Book.Types[0], page_weight + 100)

    @classmethod
    def Paperback(cls,name,paper_weight):
        return cls(name,cls.Types[1],paper_weight + 50)    

    @classmethod
    def E_book(cls,name,size):
        return cls(name,cls.Types[2],size)


book = Book.hardcore("Python",200)
book1 = Book.Paperback("Java",100)
book2 = Book.E_book("PHP","40 MB")
print(book)
print(book1)
print(book2)



# n = 2

# m = 5

# for x in range(0,10):
#     print(n + 2)

#     for v in range(5):
#         print(m)



   