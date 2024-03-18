class A:
	def __init__(self):
		self.list1=[]

	def  input(self):
		n=int(input("Enter the number of elements in the list:"))
		for i in range(0,n):
			ele=int(input("Enter the value:"))
			self.list1.append(ele)
		print("list=",self.list1)

	def __add__(self,other):
		newlist=[]
		for i in range(0,len(self.list1)):
			newlist.append(self.list1[i] + other.list1[i])
		print("Addition of lists=", newlist)

	def __sub__(self,other):
                newlist=[]
                for i in range(0,len(self.list1)):
                        newlist.append(self.list1[i] - other.list1[i])
                print("Addition of lists=", newlist)

	def __mul__(self,other):
                newlist=[]
                for i in range(0,len(self.list1)):
                        newlist.append(self.list1[i] * other.list1[i])
                print("Addition of lists=", newlist)

	def __floordiv__(self,other):
                newlist=[]
                for i in range(0,len(self.list1)):
                        newlist.append(self.list1[i] // other.list1[i])
                print("Addition of lists=", newlist)
