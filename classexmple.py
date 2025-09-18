class employee:   #creatin a class .(blueprint)


    def putdata(self):    #This method will take input from the user and save it inside the object.
        self.id=int(input('enter the emp id = ')) #taking the emp id and store it in self.id
        self.name=input('enter the emp name = ')   #taking the emp name and store it in self.name
        self.salary=float(input('enter the emp salary = '))   #taking the emp salary and store it in self.salry



    def display(self):   #This is the another method used to display the details of employee 
        print('emp id',self.id)
        print('emp name',self.name)
        print('emp salary',self.salary)

a=employee()  #object of class employee
a.putdata()   #to enter ID, Name, Salary, and stores them in a.
a.display()     #to diplay those details

emp1 = employee()
emp1.putdata()
emp1.display()

emp2 = employee()
emp2.putdata()
emp2.display()


# print(type(a))