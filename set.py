names= {"sia", "tia", "mia"}
print(names)  #will print it in random order
print(len(names))  #print length of set
print(type(names))   #print datatype


#to access items in set
for x in names:
    print(x)


#to check if given item is there in set
if "sia" in names:
    print("Siya is there")    


#to add element in set
names.add("ara")
print(names)


#to add another list in set
names_list=["kara", "jiya"]
names.update(names_list)
print(names)


#to remove element
names.remove("kara")
print(names)