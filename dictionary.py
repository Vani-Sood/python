#creating a dictionary
phones = {
    "john" : 1223,
    "ace" : 3422,
    "ria" : 3421
}
print(phones)
print(type(phones))
print(len(phones))



#access items in dictionary
print(phones["ace"])  #will print number of ace
print(phones.get("ace"))   #will print number of ace
print(phones.keys())   #will print all values