#function
#A function is a block of code which only runs when it is called.
#You can pass data, known as parameters, into a function.
#A function can return data as a result.
#In Python a function is defined using the def keyword:


def hello():
    print('This hello world is displayed using function')
hello()

print('----------------------------------------------------')


def gopika():
    print('This is gopika')
gopika()

print('----------------------------------------------------')

#Arguments

#Information can be passed into functions as arguments.
#Arguments are specified after the function name, inside the parentheses.
#we can add as many arguments as you want, just separate them with a comma.

#parameter and arguments
#The terms parameter and argument can be used for the same thing: information that are passed into a function.
#From a function's perspective:
#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.


#function with 1 argument
def displayName(userName):
    print('my name is ' +userName)
displayName('Gopika')
displayName('Meera')
displayName('Teena')

print('----------------------------------------------------')

#function with 1 argument
def my_func(username,email):
    print('my name is ' + username + ' and email is ' + email)
my_func('Gopika','gopika@gmail.com')
my_func('Meera','meera@gmail.com')
my_func('Teena','teena@gmail.com')

print('----------------------------------------------------')

#Arbitrary Arguments, *args
#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

#This way the function will receive a tuple of arguments, and can access the items accordingly:

def details(username,*email):
    print('my name is ' +username)
    print( email ) #the email and phone number appeared as a tuple.prints the tiple itself
    #print(*email)  #unpacks the tuple and prints items separately
details('Gopika','gopika@gmail.com',859034)
details('Meera','meera@gmail.com',6578393)
details('Teena','teena@gmail.com',620034)

print('----------------------------------------------------')

print('Arbitrary Keyword Arguments, *')

def details(username,*email):
    print('my name is ' +username)
    print( email[1] ) #email is tuple so that we can use indexing on that while we do like this it display the value at the
                    #email[1] position here that is phone number it doesn't display the email id.
details('Gopika','gopika@gmail.com',859034)
details('Meera','meera@gmail.com',6578393)
details('Teena','teena@gmail.com',620034)

print('----------------------------------------------------')

print('Arbitrary Keyword Arguments, **')
#If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:

def unknownargs(**args):
    print(args)
unknownargs(name='gopika',email='gopika@gmail.com',phone=6890034329,address='periye',district='ksd',country='india')

print('----------------------------------------------------')

#Default Parameter Value
#The following example shows how to use a default parameter value.
#If we call the function without argument, it uses the default value:
print('----------Default arguments--------')
def my_country(country = "india"):
    print('i am from ' + country)
my_country("norway")
my_country("canada")
my_country()  #here we didn't give the country name so when this function called the default value will be stored by the defult value
my_country("london")
my_country("swedan")
my_country()  #here we didn't give the country name so when this function called the default value will be stored by the defult value


print('----------------------------------------------------')

def addition(x,y):
    sum= x+y
    return sum
    #return x+y
n1=int(input('enter the number1= '))
n2=int(input('enter the number2= '))
add=addition(n1,n2)
print(add)

print('----------------------------------------------------')

def fact(num):
    if num==0:
        return 1
    factorial=num*fact(num-1)
    return factorial
n1=int(input('enter the number1= '))
factnum=fact(n1)
print(factnum)

print('----------------------------------------------------')

def oddeven(num):
    if num%2==0:
        return num,' is even'
    else:
       return num,' is odd'
n1=int(input('enter the number1= '))
oddevennum=oddeven(n1)
print(oddevennum)

print('----------------------------------------------------')
