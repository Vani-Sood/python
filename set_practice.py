#Given three arrays, we have to find common elements in three sorted lists using sets. 
#Input: arl = [1, 5, 5] ar2 = [3, 4, 5, 5, 10] ar3 = [5, 5, 10, 20] 
#Output: [5]
s1={1, 5, 5}
s2={3, 4, 5, 5, 10}
s3={5, 5, 10, 20}
print(s1.intersection(s2, s3))   # This returns a new set containing elements common to all given sets.