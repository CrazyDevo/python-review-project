person_info=("Adam",34,True)

print(type(person_info))
print(person_info[0])
print(person_info[1])
print(person_info[2])
# print(person_info[3])

#person_info[0]="Mustafa"
#print(person_info[0])

list1=["A","B",True,34,2.5]

print(list1[3])

print(type(list1))

name="Adam"

list2=list(name)

print(list2)
print("-----------------------------------------")
for each in list1:
    print(each)

print("---------------------")

for x in range(5,10):
    print(x)

print("-------------------")
for each_char in "Adam":
    print(each_char)