d={}

class employee:
	def input(self):
		self.name=input("Enter the name of the Employee\n")
		self.address=input("Enter the address of the employee\n")
		self.pan=input("Enter the Pan number of the employee\n")
		self.bs=int(input("Enter the basic salary of the employee\n"))
		self.tds=int(input("Enter the tds of the employee\n"))
		self.deduct=int(input("Enter the deduction amount\n"))
		self.hra=1.25*self.bs
		self.da=0.25*self.bs
		self.gross=self.bs+self.hra+self.da
		self.net=self.gross-self.deduct
		self.update()

	def update(self):
		d.update({self.name:{"Name":self.name,
			"Address":self.address,
			"Pan":self.pan,
			"Basic Salary":self.bs,
			"TDS":self.tds,
			"Deductions":self.deduct,
			"HRA":self.hra,
			"DA":self.da,
			"Gross Salary":self.gross,
			"Net Salary":self.net}})

	def search(self,name):
		for key in d:
			if key==name:
				print("Employee Found")
				print(key,d[key])
				break
		else:
			print("Employee not found")

	def printemp(self):
		for key in d:
			print(key,d[key])



em=employee()

while True:
	print("\n1.Enter the Employee Details\n2.Search For theEmployee\n3.Display all Employees\n")
	ch=int(input("Enter your choice:\n"))
	if ch==1:
		em.input()
	elif ch==2:
		name=input("Enter the name to be searched\n")
		em.search(name)
	elif ch==3:
		em.printemp()
	else:
		print("invalid")
		break
