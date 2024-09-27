f=1
l1=tuple(input("Enter the tuple:"))
while(f):
	print("_____MENU------------");
	print("1.Concatenation")
	print("2.Repetition")
	print("3.Slicing")
	print("4.Range slicing")
	print("5.Length of tuple")
	print("6.Membership")
	print("7.Iteration")
	print("8.Maximum value")
	print("9.Deleting a tuple")
	ch=int(input("Enter your choice:"))
	if(ch==1):
		l2=(5,6,"college of engineering")
		print("Concated tuple is:",l1+l2)
	elif(ch==2):
		print("Repeted tuple is:",l1*2)
	elif(ch==3):
		print("Sliced tuple is:",l1[2])
	elif(ch==4):
		print("Ranged slice:",l1[1:3])
	elif(ch==5):
		print("Length of tuple:",len(l1))
	elif(ch==6):
                print("if RVCE is there in tuple:","RVCE" in l1)
	elif(ch==7):
		print("Iteration\n")
		for i in l1:
			print(i)
	elif(ch==8):
		print("Max value:",max(l1))
	elif(ch==9):
		print(l1)
		del l1
		print("\nDeleting a tuple:")
	else:
		print("invalid choice")
		f=0
print("\nfinished")
