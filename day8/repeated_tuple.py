tup=(0,45,32,45,76,87,56,56)
my_list=[]
for i in range (len(tup)):
    count = tup.count(tup[i])
    if count >1 and tup[i] not in my_list:
        my_list.append(tup[i])

print(my_list)