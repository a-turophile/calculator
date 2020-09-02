from add import add
from subtract import subtract
from multiply import multiply
from divide import divide

print("***CALCULATOR***")
a = int(input("Enter num1: "))
b= int(input("Enter num2: "))

ch = int(input("Enter your choice:\n\t1. Addition \n\t2. Subtraction \n\t3. Multiplication \n\t4. Division \n"))
if(ch==1):
    print("\nThe sum of numbers is: ",add(a,b))
elif(ch==2):
    print("\nThe difference of numbers is: ",subtract(a,b))
elif(ch==3):
    print("\nThe product of numbers is: ",multiply(a,b))
elif(ch==4):
    print("\nDivision results in: ",divide(a,b))
else:
    print("\n\t\t\tPlease choose a correct option")

