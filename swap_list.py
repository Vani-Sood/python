#Given a list in Python and provided the index of the elements, write a program to swap the two elements in the list. 
#Examples: 
#Input: List = [23, 65, 19, 90], idx1 = 0, i * d * d * 2 = 2 
#Output: [19, 65, 23, 90] 
#Input: List = [1, 2, 3, 4, 5], idx1 = 1, i * d * 2 = 4 
#Output: [1, 5, 3, 4, 2]

n= int(input("enter size of list: "))
list=[]
for _ in range(n):
    num =int(input())
    list.append(num)

idx1 = int(input("enter index1: "))  
idx2 = int(input("enter index2: "))    
print(list)


#swap
temp= list[idx1]
list[idx1]= list[idx2]
list[idx2]= temp
print(list)
