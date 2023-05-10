l = [1,2,3,4,5,6,7]
l1 = []
for i in l:
    l1.append(i**2)
print(l1)

#comprehension
#Syntax: [expression for item in iterable if condition]

#printing the square values of the list
print([i**2 for i in l])

#printing the even values
print([i for i in l if i%2==0])

#printing values of the list in upper case letter
l2 = ["kshitij", "kumar", "sunny"]
print([i.upper() for i in l2])

d = {"key1" : 1, "key2" : 2, "key3" : 3, "key4" : 4}
print(d.items())
print({k:v**2 for k, v in d.items()})
print({k:v for k, v in d.items() if v>1})