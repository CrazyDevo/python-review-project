
list1=[1,2,3,4,5,6,7]


for each in list1:
    print(each)
    if each==3:
        print("Found it")
        break


print( "------------------")
for each in range(10):
    if each%2==0:
        continue

    print(each)

list1.reverse()

list1.remove(5)

#list1.clear()


list1.insert(0,0)
list1.append(45)
print(list1)