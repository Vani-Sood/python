cp=int(input("enter cost price: "))
sp=int(input("enter selling price: "))
if cp<sp:
    print("profit by:", sp-cp)
elif cp>sp:
    print("loss by:", cp-sp)    
else:
    print("no profit, no loss")    