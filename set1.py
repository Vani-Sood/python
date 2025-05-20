s1= {"a", "b", "c"}
s2={"c", "d", "a"}
print(s1, s2)

s3=s2.union(s1)   #will print union
print(s3)


#OR will print union
s1.update(s2)
print(s1)


