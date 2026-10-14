# #file operations
# #opening
# file=open("file1.txt","w",encoding="utf-8")#file name,mode,encoding
# #methods
# file.write("Hello, World!")
# file.close();
# file=open("C:\\Users\\nared\\OneDrive\\Desktop\\📄\\folder\\AI-Engineering\\phase-1-python\\file.txt","r",encoding="utf-8")
# print(file.read())
# file.close()
# file=open("file1.txt","a+",encoding="utf-8")
# file.write("\n this is a new line")
# file.seek(0)  # Move the file pointer to the beginning
# print(file.read())
# file.close()

# #but instead of using open and close we can use with statement which automatically closes the file after the block is executed
# with open("file1.txt","w+",encoding="utf-8") as file:
#     file.write("this text is beig overwritten with existing files text")
#     file.seek(0)
#     content=file.read()
#     print(content)
# with open("practice.txt","r",encoding="utf-8") as file:
#     print(file.read())

# with open("practice.txt","a+",encoding="utf-8") as file:
#     file.write("\nPython is useful for AI Engineering")
#     file.seek(0)
#     print(file.read())
# with open("practice.txt","w+",encoding="utf-8") as file:
#     file.write("new contents")
#     file.seek(0)
#     print(file.read())

# #read() readline readlines() methods
# with open("file1.txt","r",encoding="utf-8") as file:
#     content=file.read()
#     file.seek(0)
#     fl=file.readline()
#     sl=file.readline()
#     file.seek(0)
#     list=file.readlines()
#     print(content)
#     print(fl)
#     print(sl)   
#     print(list)

# with open("practice.txt", "r", encoding="utf-8") as file:
#     print(file.tell())   # Usually 0 at the beginning
#     print(file.read(2))  # ne
#     print(file.tell())   # Position after reading
#     file.seek(0)         # Return to the beginning
#     print(file.read())   #new contents

#error handling
try:
    age=int(input("Enter your age:"))
    print("Your age is:",age)
except ValueError:
    print("please enter a valid Integer")

#we can also use multiple except blocks to handle different types of exceptions
try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid number.")

else:
    print(f"Your number is {number}")
    print(f"Double: {number * 2}")
finally:
    print("Cleanup runs here.")
#in above code else excutes only if try block executes successfully without any exception

def calculate_average(marks):
    if not marks:
        raise ValueError("Marks cannot be empty.")

    return sum(marks) / len(marks)

try:
    average = calculate_average([])
except ValueError as error:
    print(f"Could not calculate average: {error}")