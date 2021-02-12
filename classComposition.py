class Bookshell:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"Bookshell with {len(self.books)} books"

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"books {self.name}"    

book = Book("python")
book1 = Book("Aabid")

book2 = Book("python")
book3 = Book("Aabid")
shell = Bookshell(book,book1,book2,book3)

print(shell)


class Inner:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person name {self.name} and age is {self.age}"



class display(Inner):
    def __init__(self, name, age):
        super().__init__(name, age)
        
         

disp = display(name="Aabid",age=22)
print(disp)