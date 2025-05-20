phones = {
    "john" : 1223,
    "ace" : 3422,
    "ria" : 3421
}
print(phones)
#update phone of ace
phones["ace"]= 1234
print(phones)


#add element in list
phones["kia"]= 5744
print(phones)

#add another dictionary in existing dictionary

more_phones= {
    "siya" : 1229
}
phones.update(more_phones)
print(phones)

#remove elements in dictionary
phones.pop("ace")
print(phones)
#remove last element
phones.popitem()
print(phones)

#to empty entire dictionary
phones.clear()
print(phones)