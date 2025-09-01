matrix = [[1,2,3], [4,5,6],[7,8,9]]
print(matrix)
for i in matrix:
    print(i)

    # list indexing
matrix = [[1,2,3], [4,5,6],[7,8,9]]
print(matrix)
for i in range(len(matrix)):    #len(matrix) gives the row length
    for j in range(len(matrix[0])):    #len(matrix[0]) gives the col length
        print(f"matrix[{i}][{j}] = ",matrix[i][j])   # f"....." called f-string lets us directly inserts variable inside the { }



# Matrix Addition
print("Matrix addition")
m1 = [[1,2,3],[4,5,6]]
m2 = [[7,8,9],[1,2,3]]
for i in range(len(m1)):
    print((m1[i][0]))
for i in m1:
    print(i)
for i in  m2:
    print(i)

add=[[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len((m1)))]
print("Added matrix is ",add)

sub=[[m2[i][j] - m1[i][j] for j in range(len(m1[0]))]for i in range(len((m1)))]
print("substracted matrix is",sub)




print('----------------matrix multiplication--------------------')
# x[0][0]*y[0][0] + x[0][1]*y[1][0] + x[0][2]*y[2][0] = X00
# x[0][0]*y[0][1] + x[0][1]*y[1][1] + x[0][2]*y[2][1] = X01
# x[0][0]*y[0][2] + x[0][1]*y[1][2] + x[0][2]*y[2][2] = X02

# x[1][0]*y[0][0] + x[1][1]*y[1][0] + x[1][2]*y[2][0] = X10
# x[1][0]*y[0][1] + x[1][1]*y[1][1] + x[1][2]*y[2][1] = X11
# x[1][0]*y[0][2] + x[1][1]*y[1][2] + x[1][2]*y[2][2] = X12

# x[2][0]*y[0][0] + x[2][1]*y[1][0] + x[2][2]*y[2][0] = X20
# x[2][0]*y[0][1] + x[2][1]*y[1][1] + x[2][2]*y[2][1] = X21
# x[2][0]*y[0][2] + x[2][1]*y[1][2] + x[2][2]*y[2][2] = X22

A=[[2,4,6],[3,7,9],[1,2,8]]
B=[[9,8,7],[1,6,3],[4,2,8]]
z=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        sum=0
        for k in range(0,3):
            sum +=  A[i][k] * B[k][j]
        z[i][j]=sum
print("Multipiled matrix is = \n",z)
# for i in z:        
#     print(i)
