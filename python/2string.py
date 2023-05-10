mystr = "harry is good boy"
print(mystr)
# # print(mystr[0::2])
# print(mystr[::-1]) #reversing the string
# print(len(mystr))

print(mystr.isalnum()) 

d = int(input("enter the number : "))
str_num = str(d)
a = 0
for i in range(0, len(str_num)):
    x = str_num[i]
    a += int(x)

print(a)
