 #strings
#variable iniatialisation
#same variable with different datatype values the 
# variable stores the value that we entered at last
x=5
print(x,type(x))

x="gopika"
print(x,type(x))

x=8.9
print(x,type(x))

x=9+3j
print(x,type(x))


# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# both are same 
y="Gopika"
z='Gopika'
print(y)
print(z)

# single line representation of a string
print('single line representation of a string')
Address1="Vayaravalli House","P.O Periye"
Address2='Periye Bazar'
print(Address1)
print(Address2)
print("India, Kerala")

c,v,n,m=5,8.9,9+3j,'Gopika'
print(c)
print(v)
print(n,m)



# multiline representation of string with single quotation mark
print('multiline representation of string with single quotation mark')
Address3='''Kasaragod 
kerala
india'''
print(Address3)

# multiline representation of string with double quotation mark
Address4="""Kerala
India
Asia"""
print(Address4)

# TYPE CONVERSION
s=5
a=float(s)
b=str(s)
c=complex(s)
print(a,type(a))
print(b,type(b))
print(c)




mul= [[sum(m1[i][k] * m2[k][j] for k in range(len(m2))) 
      for j in range(len(m2[0]))] 
     for i in range(len(m1))]
print("multiplied matrix is = ",mul)
# for i in mul:
    # print(mul)