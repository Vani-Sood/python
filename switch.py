num1= int(input("enter 1st no."))
num2= int(input("enter 2nd no."))
operator= input("enter a operator")
match operator:
    case "+":
        print("sum is ", num1 + num2)
    case "-":
        print("diff is ", num1 - num2)
    case "*":
        print("product is ", num1 * num2)
    case "/":
        print("division is ", num1 / num2)    
    case _:
        print("enter a valid operator ")
    
