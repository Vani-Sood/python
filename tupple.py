colours= ("red", "green", "blue", "red")
#we can create a single tupple after add , 
fruit=("apple",)
#to check type 
print(type(colours))
#to print length
print(len(colours))
#accessing items in a tuple
print(colours[1])  #print item at index 1 
print(colours[-1])  #print item at index -1
print(colours[1:3])  #print item at index 1 and 2
print(colours[-2:])  #print item at index -1 to end

#to check if an item is there in tupple 
if "green" in (colours):
    print("green is there ")

#traverse in tupple
for i in colours:
    print(i)


#concatinate 2 tuples:

more_colours=("violet", "purple")
colours= colours + more_colours
print(colours)
