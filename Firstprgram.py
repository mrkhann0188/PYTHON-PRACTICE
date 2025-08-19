"""# arithematic operators 
a = 5 
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

#aditonal operators
a = 50 
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a >= b) 
print(a < b)
print(a <= b) 
#logical operators
a = 20
b = 50 
print(not True)
print(not (a>b)) 
val1 = True
val2 = False
print(val1 and val2)
print(val1 or val2)
#type conversion
a = int("2") 
b = 4.09
print(a+b)

name = input("enter your age :")
print("Your age is :",name)
val = int(input("Enter any type value ::"))
print(type(val),val) 
side = int(input("enter square side :"))

print("Area =", side ** 2) 
str = 'ayaankhan'
print(str[-9:0]) 
str = "i am studying python"
print(str.replace('m', 'u'))
str = "I am md ayaan khan" 
print(str.count ("a"))
light = input("Enter the color of light ")
if(light == 'red'):
    print("stop")
elif(light == 'yellow'):
    print("be ready")
else:
    print("go")

marks = int(input("Enter your marks : "))

if(marks >=90):
    grade ="A"
elif(marks >=80 and marks < 90):
    grade = 'B'
elif(marks >=70 and marks<80):
    grade = 'C'
else:
    grade = 'D'
print("Grade of the student is : ", grade)
    
a = int(input("Enter the vaalue of a : "))
r = a%2
if(r == 0):
    print("EVEN")
else:
    print("odd")
a =int(input("Enter first number : "))
b =int(input("Enter second number : "))
c =int(input("Enter third number : "))
if(a>b and a>c):
    print("a is greatest among three")
elif(b>a and b>c):
    print("b is greatest among three")
else:
    print("c is greatest among three")

list = ['ayaan','abacus']
list.append('ak')
list.sort()
list.sort(reverse=True)
list.reverse()
list.insert(2,'akkk')
list.remove('ak')
list.pop(2)
print(list)
tuple = ('ayaan',3,'ak')
print(tuple)

# Loop through numbers 0 to 10
for i in range(11):
    
    if i == 5:
        pass  # Placeholder for future code or to ignore this iteration without doing anything
        print("Pass: This is number 5, doing nothing.")
    
    elif i == 7:
        continue  # Skip this iteration when i equals 7
        print("This line will not be printed for i = 7 because of continue.")
    
    elif i == 9:
        break  # Stop the loop entirely when i equals 9
        print("This line will not be printed for i = 9 because of break.")
    
    # Print the number if no special condition is met
    print("Current number:", i)
    input_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
result = count_strings(input_list)
print(result)

    # Creating a sample dictionary
student = {
    "name": "Alice",
    "age": 22,
    "course": "Computer Science",
    "year": "Senior"
}

# 1. Accessing items using keys
print("Accessing items using keys:")
print("Name:", student["name"])  # Accessing value with key 'name'
print("Age:", student["age"])     # Accessing value with key 'age'

# 2. Using get()
print("\nUsing get():")
print("Course:", student.get("course"))         # Returns the value for 'course'
print("GPA:", student.get("GPA", "Not Found"))  # Returns 'Not Found' as default since 'GPA' is not a key

# 3. Using keys()
print("\nUsing keys():")
print("Keys:", student.keys())  # Prints all keys in the dictionary

# 4. Using values()
print("\nUsing values():")
print("Values:", student.values())  # Prints all values in the dictionary

# 5. Using items()
print("\nUsing items():")
print("Items:", student.items())  # Prints all key-value pairs as a list of tuples"""

def count_strings(string_list):
    # Initialize an empty dictionary to store counts
    string_counts = {}
    
    # Loop through each string in the input list
    for string in string_list:
        # If the string is already a key, increment its count by 1
        if string in string_counts:
            string_counts[string] += 1
        # If the string is not a key, add it with a count of 1
        else:
            string_counts[string] = 1
            
    return string_counts

input_list = ["apple", "banana", "apple", "orange", "banana", "apple"]
result = count_strings(input_list)
print(result)



