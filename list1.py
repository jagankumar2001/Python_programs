l1=[1,2,3]
print(l1)
f=1
while(f):
	print("MENU\n1.Concat\n2.Length of a list\n3.Add a element to a list\n4.Membership\n5.Slice\n6.Repitition\n7.Range slicing\n8.Iteration\n9.Maximum\n10.Minimum\n11.Delete\n12.Exit")
	ch=int(input("Enter ur choice:"))
	if(ch==1):
		l2=[4,5,6,7]
		print("Concatenated list is:",l1+l2)
	elif(ch==2):
		print(l1)
		print("Length of a list is:",len(l1))
	elif(ch==3):
		ele=int(input("Enter a element to be append:"))
		l1.append(ele)
		print("New list:",l1)
	elif(ch==4):
		print("checking if 4 is in list:",4 in l1)
	elif(ch==5):
		ind=int(input(f"Enter the index less than {len(l1)}:"))
		print("The element is :",l1[ind])
	elif(ch==6):
		print("Repetition of list for two times is:",l1*2)
	elif(ch==7):
		print("Elements from index 1 to 3 is:",l1[1:3])
		print(l1)
	elif(ch==8):
		for i in range(len(l1)):
			print(i)
	elif(ch==9):
		print("Maximum value:",max(l1))
	elif(ch==10):
		print("Minimum value:",min(l1))
	elif(ch==11):
		del l1
		print(l1)
	elif(ch==12):
		f=0
	elif(ch==13):
		l1.sort()
		print("Sorted element is :",l1)
	else:
		print("Invalid choice")
print("Finished")
