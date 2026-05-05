# Harvard-CS50

**Lecture 1 Notes (Functions and Variables)**
```python
#%% Strings (str)
name = input("What's your name? ").strip().title()
first, last = name.split(" ")    # split at spaces
"""
.strip() removes left and right extra spaces from str
.capitalise() capitalises first word of str
.title() capitalises every word of str 
.split() splits str into multiple substrings
"""
print("Hello, " + first + " " + last)     # concatenation (+ " " +  to include space)
print("Hello,", first)
print("Hello, ", end="")     # named parameter of print (end="\n" by deafult)
print(first)
print(f"Hello, {first}")     # f-string

#%% Integers (int)
x = int(input("Choose x. ")) 
y = int(input("Choose y. "))
"""
Without int(), x+y would be the concatenation of x and y since input() returns a str.
"""
print(x+y)

#%% Floats (float)
x = float(input("What is x? "))
y = float(input("What is y? "))
print(round(x+y))      # round(#) rounds # to the nearest integer
print(f"{x+y:,}")      # :, formats the str with a comma each triple of digits with a comma
print(round(x/y,2))    # round(#,n) rounds # to n digits
print(f"{x+y:.2f}")    # .2f rounds to two digits

#%% Functions
name = input("What is your name? ")
def hello(person):
    print("Hello", person)
hello(name)

n = int(input("What is n? "))
def square(n):
    return n**2 # equivalent to pow(n,2)
square(n)
```

**Lecture 2 Notes (Conditionals)**

```python
"""
=  (assignment, copying right-to-left)
== (equality, comparing left and right)
!= (not equal to)
"""
x = int(input("What's x? "))
y = int(input("What's y? "))

#%%
if x < y:
    print("x is less than y")
elif x > y: # elif (else if)
    print("x is greater than y")
else:
    print("x is equal to y")

#%%
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

#%%
if x == y :
    print("x is equal to y")
else:
    print("x is not equal to y")

#%%
score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

#%%
def main():
    n= int(input("n: "))
    if is_even(n):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False
    
def is_even_pythonic(n):
    return True if n%2 == 0 else False

def is_even_pythonic_best(n):
    return n%2 == 0

main()

#%%
name = input("What's your name? ")
 
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

**Lecture 3 (Loops)**

```python
#%% While loop (counting down).
i = 3
while i != 0:
    print("meow")
    i -= 1  # i.e. i=i-1
#%% While loop (counting up).
i = 0
while i < 3:
    print("meow")
    i += 1  # i.e. i=i+1
#%% For loop.
for _ in range(3): # range(n) returns n values
    print("meow") 
#%% Pythonic answer.
print("meow\n" * 3, end="")

#%%
def main():
    number = get_number()
    meow(number)
def get_number():
    while True:
        n = int(input("n: ")) 
        if n > 0:
            break
    return n
def meow(n):
    for _ in range(n):
        print("meow")

#%%
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i+1, students[i])
    
# Add an element to a list.
students.append("Draco")
print(students)
# Remove an element from a list.
students.remove("Draco")
print(students)
# Add an element to a list at a specified index.
students.insert(0,"Luna") 
print(students)
# Add a list to a list.
students.extend(["Draco", "Snape"])
print(students)
# Reverse the order of a list.
students.reverse()
print(students)

# List comprehensions.
lowercase_students = [name.lower() for name in students]
print(lowercase_students)
long_names = [name.lower() for name in students if len(name) > 4]
print(long_names)
# Dictionary comprehension.
student_dict = {name: "HP" for name in students}
print(student_dict)

#%% Dicitionary (dict) 
"""
{}, i.e. curly brackets
"key":"value"
"""
# A dicitionary with one set of values (houses).
students = {
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco": "Slytherin"}
 
for student in students:
    print(student) # prints keys
    
for student in students:
    print(students[student]) # prints values
    
for student in students:
    print(student, students[student], sep = ", ")

# A dictionary with two sets of values (house and patronus).
students_TwoValues = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}  # Draco has no patronus.]

for student in students_TwoValues:
    print(student["name"], student["house"], student["patronus"], sep = ", ")
#%%
def main():
    #print_column(3)
    #print_row(4)
    print_square(3)

def print_column(height):
    print("# \n"*height, end="")

def print_row(width):
    print("?"*width)
   
def print_square(size):
    for _ in range(size):
        print("#"*size)
main()

#%% Dictionary manipulation.
fleet = {
    "ship": "USS Enterprise", 
    "registry": "NCC-1701-D",
    "captain": "Jean-Luc Picard"}

# Return the number of keys.
print(len(fleet)) 
# Return value associated to key=ship.
print(fleet.get("ship")) # equivalent to fleet["ship"]
# Add key/value to dictionary.
fleet.update({"length": "641 m"}) 
# Remove key from dictionary.
fleet.pop("captain") # .clear() removes all keys

print(", ".join(fleet.keys()))   # .keys() returns all keys
print(", ".join(fleet.values())) # .values() returns all values
```
