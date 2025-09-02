n = int(input("enter the number = "))
b = int(input("enter the base = "))

quot = n
rem = []

while quot > 0:
    rem.append(quot % b)
    quot = quot // b

if b == 2:
    print("binary of", n, "=", rem[::-1])
elif b == 8:
    print("octadecimal of", n, "=", rem[::-1])
elif b == 16:
    print("hexadecimal of", n, "=", rem[::-1])
else:
    print("not applicable")
