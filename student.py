class student:
    def __init__(self,my_roll,my_name,my_marks):

        self.rollno=my_roll

        self.name=my_name

        self.marks=my_marks

    def average(self):

        return sum(self.marks)/len(self.marks)
first_student= student(1,'varun',[50,60,70,80,90])

print(first_student.rollno,first_student.name)

print(first_student.average())