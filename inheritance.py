print('----------------------inheritance-------------------------------')
#Inheritance is a fundamental concept in object-oriented programming (OOP)
#that allows a class (called a child or derived class)
#to inherit attributes and methods from another class (called a parent or base class).

#TYPES Of Inheritance
#Single Inheritance
    #In single inheritance, a child class inherits from just one parent class.

#Multiple Inheritance
    #In multiple inheritance, a child class can inherit from more than one parent class.

#Multilevel Inheritance
    #In multilevel inheritance, a class is derived from another derived class (like a chain).

#Hierarchical Inheritance
    #In hierarchical inheritance, multiple child classes inherit from the same parent class.

#Hybrid Inheritance
    #Hybrid inheritance is a combination of more than one type of inheritance.



class Cars:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(self.name + " " ,self.price)   #here we doesnt return the value we print it here so 
c1=Cars("defender","40lakh")
c1.display()  # so we display it like this  


print('----------------------------------------------------------------------------------------------------------------')


#parent --> child
class Car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(self.name + " ",self.price)


#here we create an empty class called Bikes but we inherits the properties of the class Car
class Bikes(Car):
    pass                
b1=Bikes("Duke 390","4lakh")
b1.display()

print('----------------------------------------------------------------------------------------------------------------')

# class Car:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def display(self):
#         print(self.name + " ",self.price)


#here we create an __init__ function and make it as empty after that it takes the values for the arguments.
# then its try to make display it goes to the parent class display function but there is sel.m=name and self.price but we didnt mentioned it anywhere in the child class 
# so it make error .
# class Bikes(Car):
#     def __init__(self, name, price):
#          pass                
# b1=Bikes("Duke 390","4lakh")
# b1.display()


#fix the above error
class Car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(self.name + " ",self.price)

class Bikes(Car):
    def __init__(self, name, price):
         self.name=name
         self.price=price             
b2=Bikes("Duke 390","4lakh")
b2.display()

print('----------------------------------------------------------------------------------------------------------------')

#we can inherit the __init__ function only of the parent class

class Car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(self.name + " ",self.price)

class Bikes(Car):
    def __init__(self, name, price):
         Car.__init__(self,name,price)          
b2=Bikes("bullet","4lakh")
b2.display()

print('---------------------------------------------------------------------------------------------------------------')


#we can inherit all the properties to inside of a init function in the child class using super()  function
#Super()
#super() function is used to call the parent class’s methods. 
# In particular, it is commonly used in the child class’s __init__() method to initialize inherited attributes. 
# This way, the child class can leverage the functionality of the parent class.

class Car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(self.name + " ",self.price)

class Bikes(Car):
    def __init__(self, name, price):
         super().__init__(name,price)     #by using super() fuction we inherits all the methods and properties inside the parent class
b3=Bikes("Himalaya","4lakh")
b3.display()

print('-------------------------------------------------------------------------------------------------------')

class Car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def display(self):
        print(self.name + " ",self.price)

class Bikes(Car):
    def __init__(self, name, price,buyer):
         super().__init__(name,price)    #by using super() fuction we inherits all the methods and properties inside the parent class
         self.buyer=buyer                #create another parameter and assign it into a variable called self.buyer
    def purchsedetails(self):            #instead of display it through parent class we create a seperate function to display the model,price,and buyer
        print("model : ",self.name)
        print("price : ",self.price)
        print("buyer : ",self.buyer)
        
b4=Bikes("Himalaya","4lakh",'Gopika')   ## creating object for class bike(child class)
b4.purchsedetails()                     #call the fuction to display the details



