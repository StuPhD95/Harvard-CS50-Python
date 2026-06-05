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

**Lecture 3 Notes (Loops)**

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


**Lecture 4 Notes (Exceptions)**

```python
"""
SyntaxError -> code isn't written in valid Python, e.g. print("Hello)
ValueError  -> the argument is invalid, int("Hello")
NameError   -> unrecognised variable or function, e.g. print(x) when x hasn't been defined
"""
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x # Return is stronger than break.
        except ValueError:
            print("x is not an integer")
            
def get_int_pass(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x 
        except ValueError:
            pass # Instead of alerting the user that x is not an integer, just provide another input.
main()

#%%
def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(1,n+1):
        print(i, end=" ")
        print("#" * i)
main()

#%%
def get_pace(miles, minutes):
    if minutes < 0: 
        raise ValueError("Minutes must be greater than 0.")
    return minutes/miles
```

**Lecture 5 Notes (Libraries)**

``` python
import random  # import module

coin = random.choice(["H","T"]) # Uniform probability. 
print(coin)

die = random.randint(1,6) # Uniform probability.
print(die)

cards = ["J", "Q", "K"]
# .choices = uniformly take two elements of a list WITH replacement 
print(random.choices(cards,k=2))              
# weights=[] allows for non-uniform probability       
print(random.choices(cards,weights=[80,10,10,],k=1)) 
# .sample = uniformly take two elements of a list WITHOUT replacement
print(random.sample(cards,k=2))                     
# .shuffle = uniformly rarrange a list
random.shuffle(cards) 
for card in cards:
    print(card, end = " ")
#%%
from random import choice  # from module import function

coin = choice(["H","T"])
print(coin)
#%%
import statistics

marks = [100, 90]
print(statistics.mean(marks))
#%% 
import sys 

if len(sys.argv) < 2:
    sys.exit("Too few arguments.")
    
for arg in sys.arv[1:]: # range(1,len(sys.arv)) would also work
    print("Hello, my name is", argv) # argv[0] = name of file you're executing
    
#%% PyPI = "Python Package Index" 
# pip install cowsay 
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
    cowsay.trex("Hello, " + sys.argv[1])
    
#%% API = "Application Program Interface" 
# pip install requests
import requests
import sys 
import json # JSON = JavaScript Object Notation

if len(sys.argv) != 2:
    sys.exist()
    
response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.arvg[1])
content = response.json()
for result in content["results"]:
    print(result["trackName"])

#%% sayings.py
def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}.")
    
def goodbye(name):
    print(f"Goodbye, {name}.")

if __name__  == "__main__": # __name__ -> main() will not run if this file is imported into another file (i.e. next cell)
    main()

#%%
import sys
import sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
```

**Lecture 6 Notes (Unit Tests)**

```python
#%% calculator.py
def main():
    x = int(input("What's x? "))
    print(f"x squared is {square(x)}")

def square(n):
    return n * n  # n + n for testing purposes

if __name__ == "__main__":
    main()

#%% test_calculator.py
from calculator import square

def main():
    test_square()

"""
Takeaway: too many lines of code to test the square function
Solution: pytest module
"""   

def test_square(): # It's convention to name the function in this way.
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")   
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")    
    try:
        assert square(-2) == 4
    except AssertionError:
            print("-2 squared was not 4")      
    try:
        assert square(-3) == 9
    except AssertionError:
            print("-3 squared was not 9")     
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
        
if __name__ == "__main__":
    main()

#%% test_calculator_pytest.py
from calculator import square
import pytest 

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0 

# run: pytest test_calculator_pytest.py
# return: first failure in test_square

#%%
def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    
def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    
def test_zero():
    assert square(0) == 0 
    
def test_str():
    with pytest.raises(TypeError):
        square("cat")
           
# run: pytest test_calculator_pytest.py
# return: first failure in test_positive, test_negative, test_zero and test_str

#%% hello.py
def main():
    name = input("What's your name? ")
    print(hello(name))
    
def hello(to = "world"):
    return f"Hello, {to}"
    
if __name__ == "__main__":
    main()

#%% test_hello.py
from hello import hello

def test_default():
    assert hello() == "Hello, world"
    
def test_argument():
    assert hello("Stuart") == "Hello, Stuart"

def test_hogwarts():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"Hello, {name}"
    
# run: pytest test_hello.py
# __init__.py in a folder tells Python to treat that folder as a package (multiple modules inside a folder)
# run: pytest FolderName
```

**Lecture 7 Notes (File I/O)**

```python
names = []

for _ in range(3):
    names.append(input("What's your name? ")) # Repeat 3 times.

for name in sorted(names): # Note: sorted() supports a key parameter for custom sorting.
    print(f"Hello, {name}.")

#%%
name = input("What's your name? ")

with open("names.txt", "a") as file:   # "a" = append to names.txt
    file.write(f"{name}\n" )           # Unlike print, write doesn't insert new lines.
# file.close() isn't needed if "with" statement is inserted

#%%
with open("names.txt", "r") as file:  # "r" = read names.txt (DEFAULT)
    lines = file.readlines() # readlines() method returns a list
    
for line in lines:
    print("Hello,", line.rstrip()) # Remove the new line in names.txt. Could also use end="".
    
# Or more compactly... 

with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.strip())
        
#%%
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
        
for  name in sorted(names):
    print(f"Hello, {name}.")

# Or more compactly...

with open("names.txt") as file:
    for line in sorted(file):
        print("Hello,", line.rstrip())
        
#%% CSV = comma separated values
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",") # split() returns a list
        print(f"{row[0]} is in {row[1]}")
        # or more readable...
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        
#%%
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")
for student in sorted(students):
    print(student)

# or by creating a dictionary...

students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house} # Create dictionary.
        students.append(student)
def get_name(student):
    return student["name"]
for student in sorted(students, key = get_name):
    print(f"{student['name']} is in {student['house']}") # Single quotes needed as double quotes are already used.
   
# or with an lambda (anonymous) function

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")        

# or using the csv module to deal with corner cases...

import csv     
       
students = []
with open("students.csv") as file:
    reader = csv.reader(file) # DictReader to read file as a dictionary.
    for name, house in reader:
        students.append({"name": name, "house": house})
        
for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")        
        
#%%
import csv

name = input("Name: ")
home = input("Home: ")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])        

# or with DictWriter...
        
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name": name, "home": home})        
        
#%%
import sys
from PIL import Image # PIL module allows Python to manipulate images.

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
    
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duraction=200, loop=0)
```
