class operover:
	def __init__(self):
		self.list=[]
	def getElement(self):
		n=int(input("Size of list:"))
		for i in  range(0,n):
			ele=int(input("Enter the element:"))
			self.list.append(ele)
		return self.list
	def __add__(self,other):
		newlist=[]
		for i in range(0,len(self.list)):
			newlist.append(self.list[i]+other.list[i])
		return newlist
	def __sub__(self,other):
                newlist1=[]
                for i in range(0,len(self.list)):
                        newlist1.append(self.list[i]-other.list[i])
                return newlist1

