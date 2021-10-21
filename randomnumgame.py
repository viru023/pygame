import random

num1 = random.randint(1,10)
as_string = str(num1)
for i in range(3):
    num2 = int(input("enter a number: "))
    if num1 == num2:
        print("correct")
    else:
        print("random number is " +as_string)
        print("try again!!!")
    i-=1
print("no more lives")
