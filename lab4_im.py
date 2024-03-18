from lab4 import *

obj1=A()
obj2=A()

obj1.input()
obj2.input()

if len(obj1.list1)==len(obj2.list1):
	while 1:
		print("1. Addition\n2.Subtraction\n3.Multiplication\n4.Floor division\n5.exit")
		ch=int(input("Enter your choice:"))
		if ch==1:
			obj1.__add__(obj2)
		elif ch==2:
			obj1.__sub__(obj2)
		elif ch==3:
			obj1.__mul__(obj2)
		elif ch==4:
			obj1.__floordiv__(obj2)
		else:
			print("Invalid input")
			break
