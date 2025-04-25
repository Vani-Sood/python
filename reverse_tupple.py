input_tuple= ("avb", "sdf", "efe", "htr")
list=[]
#adding reversed value in a list
for x in reversed(input_tuple):
    list.append(x)
output_tuple= tuple(list)  #typecasting to tuple
print(output_tuple)    
