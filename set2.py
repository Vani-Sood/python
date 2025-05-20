s1 = {"a", "b", "c"}
s2 = {"c", "d", "e"}
#print(s1.intersection(s2))  # This will print: intersection of 2 sets

s1.symmetric_difference_update(s2)      #will print all except duplicate
print(s1)