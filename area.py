class Area:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def calcarea(self):
        Area=self.length*self.breadth
        return Area
A1=Area(5,3)
A1.length=10   ##we can repalce the value of length that we give during the time of object creation
print(A1.calcarea())

# del A1  # delete the object 
# del Area  # delete the class
# del length  #delete the property



#this is an empty class
class square:
    pass