#Dictionary
#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Dictionaries are written with curly brackets, and have keys and values.
#Dictionaries cannot have two items with the same key.
#The values in dictionary items can be of any data type.
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.


student={
    'name':'gopika',
    'year': 2025,
    'marks':[31,35,36,40]
}
print(student)

print('-------------------------------------------------------------------')


# using constructor
college=dict(name='LBS',place='KSD',course='cs')
print(college)

print('-------------------------------------------------------------------')
#Accesing items
print(student['year'])
#using get method get()
print(student.get('name'))

print('-------------------------------------------------------------------')

#accesing the keys only
print(student.keys())
print(college.keys())

print('-------------------------------------------------------------------')

#travelling through keys accesing the values only using loop
key_list=student.keys()
for i in key_list:
    values=student.get(i)
    print(values)

print('---------------------fetching the values only----------------------------------------------')
print(college.values())

dict_tuple=student.items()
for i in dict_tuple:
    print(i[0]) ##accessing the keys
    print(i[1]) ##accseing the values
print('-------------------------------------------------------------------')

print('----------------------Adding item---------------------------------------------')
student['dept']='CS'
print(student)

print('----------------------------------------------------------------------------------------------')
#update method
college['name']='KTU'
print(college)

#using update methode update()
college.update({'place':'tvm'})
print(college)

print('--------------------------------removing-----------------------------------------')
student.pop('year')
print(student)

student.popitem() ##pop the last inserted item
print(student)

print('-------------------------------------deleting---------------------------------------------------------')
# print(college)
del college
print('dict college is deleted so it is not print')


print('-------------------------------------clear--------------------------------------------------------')
student.clear()
print("empty dict",student)
