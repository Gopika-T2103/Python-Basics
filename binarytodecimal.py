
n = input("enter the binary number = ")
dec = 0
length = len(n)

for i in range(length):
    dec += int(n[i]) * (2 ** (length - 1 - i))

print("decimal of", n, "=", dec)

