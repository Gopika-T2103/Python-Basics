#tuple
#ordered
#immutable
#heterogenous
#Tuples are used to store multiple items in a single variable.
# allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1]...
#To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

y=(1,)  #tuple with one item 
print(y,type(y))

#create tuple with the tuple constructor
x=tuple((1,2,3,4,5,6))
print(x)
print(len(x))

print('----------------------------------------------------------------')

#Accessing the items 
print(x[3])
print(x[1:5])
print(x[:6])
print(x[-1::-1])

print('----------------------------------------------------------------')
#Adding items to the tuple
#tuple is immutable we cant change ,add ,insert to the tuple.
#so when we add items to the tuple first we make the tuple ---> list and make operations like add insert update remove to the list
# and then make the list back to tuple list--->tuple.ie, tuple--->list--->tuple

x=tuple((1,2,3,4,5,6))
print(x)
z=list(x)
z.append('Gopika')
print(type(z),z)
x=tuple(z)
print(x,type(x))

print('----------------------------------------------------------------')

A=("gopika","devika","meera","teena")
B=(1,2,3,4,5)
A+=B
print(A)

print('----------------------------------------------------------------')


p=("meera","teena","Tony")
q=(6,7,8,9)
R=p+q
print(R)


print('---------------------delete tuple-------------------------------------------')

z=("gopika","devika")
del z

print('-----------------------packing unpacking-----------------------------------------')
Students=("gopika","aparna","niveditha","teena")
print(Students)
w,*e=Students
print(w)
print(*e)  #by using the * we can store some datas in 1 variable this will used whenever we dont know how many items are the tuple

print('----------------------------------------------------------------')
#here first and last item are stored in 2 different variable and others ate stored in a single variable
w,*e,t=Students
print(w)
print(*e)
print(t)

print('----------------------------------------------------------------')








