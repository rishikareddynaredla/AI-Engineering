#functions
def multiply(a,b):
    return a*b

def is_even(n):
    if(n%2==0): 
        return "even"
    else:
        return "odd"

def greet(name):
    print("Hello",name)

def cel_to_fahr(c):
    return (9/5)*c+32

print(multiply(2,3))
print(cel_to_fahr(37))
print(is_even(5))
print(greet("Rishika"))

#multiple return values

def analyse_marks(marks):
    return sum(marks),sum(marks)/len(marks),max(marks),min(marks)

res=analyse_marks([10,20,30,40,50])
print(res)#defauly python returns a tuple
tot,avg,max,min=analyse_marks([10,20,30,40,50])#here tuple is unpacked into elements
print(tot," ",avg," ",max," ",min)

#scope
count = 0


def increment():
    global count
    count += 1
increment() 
print(count)
#*args and **kwargs
def calculate_sum(*args):
    print(args)
    return sum(args)


print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30, 40))

#kwargs-results a dictionary
def create_profile(**kwargs):
    return kwargs


profile = create_profile(
    name="Rahul",
    age=20,
    college="ABC College"
)

print(profile)
#lambda function

square=lambda num:num**2
print(square(2))
students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Aman", "marks": 72},
    {"name": "Priya", "marks": 91}
]

ranked = sorted(students, key=lambda student: student["marks"], reverse=True)

print(ranked)


#type hints
def calculate_average(marks: list[float]) -> float:
    
    if not marks:
        return 0.0

    return sum(marks) / len(marks)
print(calculate_average([85.5, 90.0, 78.5]))
