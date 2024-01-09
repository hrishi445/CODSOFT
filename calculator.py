#simple calculator

def add(num1,num2):
    return num1 + num2
 
def sub(num1, num2):
    return num1 - num2
 
def mul(num1, num2):
    return num1 * num2
 
def div(num1,num2):
    return num1 / num2
 
print("enter option number to perform arithmetic operation:")
print("1.add")
print("2.substract")
print("3.multiply") 
print("4.divide")


opr = int(input("enter your choice(1/2/3/4):"))
 
num1 = int(input("enter the first number:"))
num2 = int(input("enter the second number:"))
 
if opr == 1:
    print( num1,"+",num2, "= ",add(num1,num2))
 
elif opr == 2:
    print(num1,"-",num2, "= ",sub(num1,num2))
 
elif opr == 3:
    print(num1,"X",num2, "= ",mul(num1,num2))
 
elif opr == 4:
    print(num1,"/",num2, "= ",div(num1,num2))
else:
    print("incorrect option")
