
def oddeven(num):
    if num%2==0:
        return num,' is even'
    else:
       return num,' is odd'
n1=int(input('enter the number1= '))
oddevennum=oddeven(n1)
print(oddevennum)
