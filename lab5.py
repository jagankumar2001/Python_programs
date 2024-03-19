
#hierarchical Inheritance

class student:
        def __init__(self,usn,name,age):
                self.usn=usn
                self.name=name
                self.age=age

        def display(self):
                print("USN=",self.usn)
                print("name=",self.name)
                print("age=",self.age)

class ugstudent(student):
        def __init__(self,usn,name,age,sem,fee,stipend):
                super().__init__(usn,name,age)
                self.sem=sem
                self.fees=fee
                self.stipend=stipend

        def display(self):
                super().display()
                print("Semister=",self.sem)
                print("Fees=",self.fee)
                print("Stipend=",self.stipend)


class pgstudent(student):
        def __init__(self,usn,name,age,sem,fee,stipend):
                super().__init__(usn,name,age)
                self.sem=sem
                self.fee=fee
                self.stipend=stipend

        def display(self):
                super().display()
                print("Semister=",self.sem)
                print("Fees=",self.fee)
                print("Stipend=",self.stipend)

ug=ugstudent(11122112,'alice',24,2,250000,200000)

pg=pgstudent(11122112,'alice',24,2,250000,200000)

while 1:
        print("1.pg\n2.ug")
        ch=int(input("Enter your ch"))
        if ch==1:
                pg.display()
        elif ch==2:
                pg.display()
        else:
                print("Invalid")
                break


#Multi-level inheritance

class Student:
        def __init__(self):
                self.usn=None
                self.name=None
                self.age=None

        def getdata(self):
                self.usn=int(input("Enter your usn"))
                self.name=input("Enter your name")
                self.age=int(input("Enter your age"))

class abc1(Student):
        def __init__(self):
                super().__init__()
                self.s1=None
                self.s2=None
                self.s3=None
                self.s4=None
                self.s5=None

        def sub_marks(self):
                super().getdata()
                self.s1=int(input("Enter marks for subject1:"))
                self.s2=int(input("Enter marks for subject2:"))
                self.s3=int(input("Enter marks for subject3:"))
                self.s4=int(input("Enter marks for subject4:"))
                self.s5=int(input("Enter marks for subject5:"))

        def cal(self):
                total=self.s1 + self.s2 + self.s3 + self.s4 + self.s5
                percentage=(total/500)*100
                return total,percentage

class abc2(abc1):
        def display(self):
                super().sub_marks()
                total,percentage=super().cal()
                print("USN=",self.usn)
                print("name=",self.name)
                print("age=",self.age)
                print("Total marks",total)
                print("Percentage",percentage)

s=abc2()
s.display()

