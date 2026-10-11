print("hello world")
"""create variables"""
name='Rishika'
age=20
college='CMRCET'
cgpa=9.69
print(f"My name is {name}.\nI am {age} years old. \nI study at {college}. \nMy CGPA is{cgpa}.")
"""calculator"""
a=int(input("Enter first number"))
b=int(input("enter second number"))
c=input("enter the operator")
if(c=='+'):
    print(f"{a}+{b}={a+b}")
elif(c=='-'):
    print(f"{a}-{b}={a-b}")
elif(c=='*'):
    print(f"{a}*{b}={a*b}")
elif(c=='/'):
    print(f"{a}/{b}={a/b}")
elif(c=='%'):
    print(f"{a}%{b}={a%b}")

"""Even or odd"""
n=int(input("enter a number"))
if(n%2==0):
    print(f"{n} is even")
else:
    print(f"{n} is odd")

"""Grade calculator """
marks=int(input("enter marks"))
if(marks>=90):
    print("A grade")
elif(marks>=75 and marks<90):
    print("B grade")
elif(marks>=60 and marks<75):
    print("C grade")
elif(marks>=40 and marks<60):
    print(" grade")
else:
    print("Fail")

"""number guessing game """
num=42
while(True):
    guess=int(input("enter your guess number"))
    if(guess>num):
        print("your guess is too high")
    elif(guess<num):
        print("your guess is too low")
    else:
        print("your guess is correct")
        break