#using in-built functions
n=int(input("enter the decimal number = "))
print("binary conversion of",n," = ",bin(n)[2:])
print("octal conversion of",n," = ",oct(n)[2:])
print("hexadecimal conversion of",n," = ",hex(n)[2:].upper())