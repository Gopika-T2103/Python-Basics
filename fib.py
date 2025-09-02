print('----------------fibonaci series------------------------------\n')

n=int(input('enter the number = '))
a=0
b=1
if n <= 0:
    print("enter a number greather than 0")
elif(n==1):
    print('0')
elif(n==2):
    print('0 \n1')
else:
    print('0 \n1')
    sum = a + b
    for i in range(2,n):
        a=b
        b=sum
        sum= a+b
        print(sum)