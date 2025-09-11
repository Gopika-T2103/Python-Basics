#sets
#1.unordered -- Elements in a set do not have a defined order, and you cannot access them by index.
#2.mutable  --can add or remove elements from a set after it has been created.
#3.unindexible
#4.no duplicates are  --- Sets automatically handle duplicate values; if you try to add an element that already exists, it will not be added again.
#5.sets are created using {} brackets

#Sets are particularly useful for:
    #Removing duplicates: from a list or other sequence.
    #Fast membership testing: using the in keyword.
    #Performing mathematical set operations: like union, intersection, and difference.


x={"Gopika","aparna","niveditha",1,2,3,4}
print(x,type(x))

#to print the length of the set
print(len(x))

print('--------------------------')

#create set using constructor
y=set(("teena","meera","tony",1,2,3,4))
print(y,type(y))

print('--------------------------')


#duplicates are not allowed sets cannot have two items with the same value.Duplicate values will be ignored:
A = {"apple", "banana", "cherry", "apple"}
print(A)

print('--------------------------')
#adding elements to the set
x.add(7)
print(x)

print('--------------------------')

y.add("apple")
print(y)

print('--------------------------')
#Set items can be of any data type
s1 = {"apple", "banana", "cherry",True, False,1, 5, 7, 9, 3}
print(s1)
print('--------------------------')

#Accessing set items using for loop, in keyword,not in keyword

#for loop
for i in s1:
    print(i)
print('--------------------------')
print('checking if the item present in the set using "in" keyword')
print("apple" in s1 )

print('--------------------------')

print('checking if the item present or not in the set using "not in" keyword')
print("gopika" in s1 )

print('--------------------------')

print('-----------Adding items---------------')
#Once a set is created, we cannot change its items, but we can add new items.
#To add one item to a set use the add() method.

s2 = {"apple", "banana", "cherry", 5, 7, 9, 3}
s2.add("orange")
print(s2)

print('--------------------------')
#To add items from another set into the current set, use the update() method.
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.

thisset={"apple","orange","banana"}
trophical={"meera","teena","tony"}
thisset.update(trophical)
print(thisset)

print('--------------------------')


#The object in the update() method does not have to be a set, it can be any iterable object
print('Add elements of a list to at set:')
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

print('--------------------------')

print('-----------Remove set items---------------')
#To remove an item in a set, use the remove(), or the discard() method
print('using remove()')
thissets = {"apple", "banana", "cherry"}
thissets.remove("banana")
print(thissets)

#If the item to remove does not exist, remove() will raise an error.
# thisset.remove("pinapple")
# print(thisset)

#Remove "banana" by using the discard() method:
# If the item to remove does not exist, discard() will NOT raise an error.
print('using discard()')
thissets.discard("cherry")
print(thissets)

thissets.discard("orange")
print(thissets)

print('----------------------------------')
#we can also use the pop() method to remove an item, but this method will remove a random item, so we cannot be sure what item that gets removed.
# The return value of the pop() method is the removed item.
#Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
s3 = {"apple", "banana", "cherry"}

d = s3.pop()

print(d,"is the poped item")

print(s3,"set after 1 item is poped")

print('----------------------------------')
print('--------------clear--------------------')
#The clear() method empties the set:
set1 = {"apple", "banana", "cherry","Gopika"}
set1.clear()
print(set1)

print('--------------Delete--------------------')
# The del keyword will delete the set completely:
print(set1)
del set1
# print(set1)  if we print the set1 after it deleted it throws an error that set1 is not defined .it is because del set1 deletes the complete set

print('---------------------------set operations--------------------------------------------')
#Sets support various mathematical set operations:
    #Union (| or union()): Returns a new set containing all unique elements from both sets.
    #Intersection (& or intersection()): Returns a new set containing elements common to both sets.
    #Difference (- or difference()): Returns a new set containing elements in the first set but not in the second.
    #Symmetric Difference (^ or symmetric_difference()): Returns a new set containing elements that are in either set but not in both.
print('---------------------------union operation---------------------------------------')
#The union() and update() methods joins all items from both sets.
#The union() method returns a new set with all items from both sets.
#Join set1 and set2 into a new set:

set4 = {"a", "b", "c"}
set5 = {1, 2, 3}

set6 = set4.union(set5)
print(set6)

#You can use the | operator instead of the union() method, and you will get the same result
set7 = {"annie", "binny", "curly"}
set8 = {1, 2, 3}

set9 = set7 | set8
print(set9)

print('join multiple sets')
# All the joining methods and operators can be used to join multiple sets.
# When using a method, just add more sets in the parentheses, separated by commas:
# Join multiple sets with the union() method:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

print('join operation by using | ')
# When using the | operator, separate the sets with more | operators.
# The  | operator only allows you to join sets with sets, and not with other data types like you can with the  union() method.
# Use | to join two sets.

sets1 = {"ananya", "pearly", "carrie"}
sets2 = {1, 2, 3}
sets3 = {"Johnson", "Elsa"}
sets4 = {"pinapple", "bananas", "blueberry"}

mysets = sets1 | sets2 | sets3 |sets4
print(mysets)


print('---------intersection----------')
#Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets.
#You can use the & operator instead of the intersection() method, and you will get the same result.
# The & operator only allows you to join sets with sets, and not with other data types like you can with the intersection() method.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print("item in both set is",set3)

print('intersection using & ')
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print("item in both set is",set3)


print('-------difference operation (-) ------')
#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print("item in set1 but not in set2",set3)

print('-----difference operation using difference()-----')
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print("item in set1 but not in set2",set3)

