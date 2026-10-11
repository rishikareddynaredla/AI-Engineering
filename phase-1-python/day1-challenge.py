name=input("enter student name")
pymarks=int(input("enter python marks"))
matmarks=int(input("enter math marks"))
dsamarks=int(input("Enter dsa marks"))
marks=pymarks+matmarks+dsamarks
avg=marks/3
if(avg>=90):
    grade='A'
elif(avg>=80):
    grade='B'
elif(avg>=70):
    grade='C'
elif(avg>=60):
    grade='D'
else: 
    grade='F'
print(f"Student {name} has marks as follow \nPython:{pymarks}\nMaths: {mat}")