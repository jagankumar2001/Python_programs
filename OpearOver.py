import module
obj1=module.operover()
obj2=module.operover()
obj1.getElement()
obj2.getElement()
f=1
while f:
	print("----MENU----\n1.Adn2.Sub\n3.Exit")
	ch=int(input("Enter your choice:"))
	if(ch==1):
		print(obj1+obj2)
	elif(ch==2):
		print(obj1-obj2)
	elif(ch==3):
		f=0
	else:
		print("Invalid choice")
