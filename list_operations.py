import copy

l1=[1,23,4,5,6]
l2=[6,7,8,91,1]
# Append

l1.append(8)
print(l1)

#copy
l3=copy.copy(l1)
print(l3)

#clear

l3.clear()
print(l3)
print(l1)

#count

print(l2.count(1))
print(l2)
print(l1)

#insert

l2.insert(1,"Hello")
print(l2)

#pop

l2.pop()
print(l2)

#remove

l2.remove("Hello")
print(l2)

#reverse
print(l1)
l1.reverse()

print(l1)

# min
print(l1)
print(min(l1))

#max
print(l2)
print(max(l2))


#extend
print(l1)
l1.extend(l2)
print(l1)

#index

print(l1.index(6))
print(l1)



