class Student:
   def __init__(self):     #__init__ this is out method.

       self.name=45 * 2
       self.dum=22 * 2
       self.gade = (45,48,54,66,78,77)
       for c in self.gade:
           if c == 66:
               print("We found '66'")
           else:
               print("We don,t find item")

     
   def avarge(self):
        return sum(self.gade) / len(self.gade)
        
student = Student()     # here we are defining the object for Student Class and we calling our class here.
print(student.name)
print(student.dum)
print(student.avarge())  # here we are calling the avarage method with Student class Object.

user_input = input("Press Enter to Exit") 
  