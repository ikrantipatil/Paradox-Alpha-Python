num1=float(input("enter 1st no="))
num2=float(input("enter 2st no="))

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
def mod(num1,num2):
    return num1%num2
def exponent(num1,num2):
    return num1**num2
def greaterthan(num1,num2):
    return num1>num2
def lessthan(num1,num2):
    return num1<num2

print("Select operation : \n" \
      "1. add\n" \
      "2. sub\n" \
      "3. mul\n" \
      "4. div\n" \
      "5. mod\n" \
      "6. exponent\n" \
      "7. greaterthan\n" \
      "8. lessthan\n" )
      
operation=int(input("select the operation that needs to be perform from 1 to :8"))

if operation ==1:
      print("addition of two numbers is" ,add(num1,num2))
elif operation ==2:
      print("subtraction of two numbers is" ,sub(num1,num2))
elif operation ==3:
      print("multiplication of two numbers is" ,mul(num1,num2))
elif operation ==4:
      print("division of two numbers is" ,div(num1,num2))
elif operation ==5:
      print("modulas of two numbers is" ,mod(num1,num2))
elif operation ==6:
      print("exponential of two numbers is" ,exp(num1,num2))
elif operation ==7:
      print(num1, ">", num2, greaterthan(num1,num2))
elif operation ==8:
      print(num1, "<", num2, lessthan(num1,num2))
else:
      print("invalid input")



if num1>=num2:
    greaternum=num1
else:
    greaternum=num2
print("Largest number is =",greaternum)
