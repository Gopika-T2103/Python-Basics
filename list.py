# LIST
# Lists are used to store multiple items in a single variable
# List items are ordered, changeable, and allow duplicate values
# List items are indexed, the first item has index [0], the last first item has index [-1].
a=[5,10,"s"]
print(a)

b,c,d,e=[10,50,"s","text"]
print(b)
print(c)
print(d)
print(e)


# this become an error become value error because too many values to unpack
# only 4 variables are there but the values are 5 so unpacked 
# b,c,d,e=[10,50,"s","text","gopika"]
b,c,d,e=[10,50,"s","text"]
print(b,c,d,e)

list=[10,50,"s","text"]
my_list=list
print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])


# list can be created by using list() constructor
# thislist = list(("apple","banana","cherry","mango"))
# print(thislist)
# print(len(thislist))
thislist=["apple","banana","cherry","mango"]
print(thislist)
print(len(thislist))


# Access list Items

# Indexing the list items  or accessing the list items using index number
thislist=["apple","banana","cherry","mango","kiwi","strwaberry","dragon fruit"]
print(thislist[0])
print(thislist[1])
print(thislist[2])
print(thislist[3])
print(thislist)


# Negative indexing
thislist=["apple","banana","cherry","mango","kiwi","strwaberry","dragon fruit"]
print(thislist[-1]) #returns the last item

print("negative index")
print(thislist[::-1]) #returns the reversed list


# Range indexing
print(thislist[1:4])   # 1 is the startindex and 4 is end index and main thing 4 is not included range(start:stop)

print(thislist[:4])    # having only the end index so its start from the 0 th index

print(thislist[3:])    # having only the start index it dont have any end index so its start from the 3rd index till the last 


mylist = ['apple', 'banana', 'cherry']
mylist.insert(0, 'orange')   #inserts elemnt ate the 0th index
print(mylist[1])   #o/p the apple item will be come in the 1st index
 

mylist.append("goosberry")   #adding elemnt to the last of the list
mylist.append("blueberry")    #adding elemnt to the last of the list
print(mylist)


