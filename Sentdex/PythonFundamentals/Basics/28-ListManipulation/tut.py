
x = [1,2,3,4,5,6,7,8,9,10,11]
y = ["Janet","Jessy","Kelly","Alice","Joe","Bob"]

x.append(13)
x.insert(11,12)
x.remove(x[5])

print(x)
print(x[11])
print(x[2:5]) #Slicing - to access a slice
print(x[-1]) #To access the lass element of the list
print(x.index(1)) #To find the index number of a list item
print(x.count(13)) #To find how many same elements there are
x.sort() #To sort numerically or alphabetically
print(x)

y.sort()
print(y)
y.reverse()
print(y)
