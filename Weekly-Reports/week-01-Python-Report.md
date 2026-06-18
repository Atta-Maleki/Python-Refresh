# 📘 Python Week 1 — Day 1 Report

## 1. Lists — Accessing & Slicing

Lists are ordered collections and use indexing starting from 0.

### Basic slicing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

Output:
['cherry', 'orange', 'kiwi']

- Index 2 is included, index 5 is NOT included
- First element starts at index 0

---

### Negative indexing
print(thislist[-4:-1])

Output:
['orange', 'kiwi', 'melon']

- -1 is the last item
- Negative indexing starts from the end

---

## 2. Modifying Lists

thislist[1] = "blackcurrant"

thislist[1:3] = ["blackcurrant", "watermelon"]

thislist[1:3] = ["watermelon"]

thislist.insert(2, "watermelon")

---

## 3. Adding Items

thislist.append("orange")

thislist.extend(["mango", "pineapple"])

---

## 4. Removing Items

thislist.remove("banana")

thislist.pop(1)   # removes index 1
thislist.pop()    # removes last item

del thislist[0]
del thislist

thislist.clear()

---

## 5. Looping Through Lists

for x in thislist:
    print(x)

[print(x) for x in thislist]

for i in range(len(thislist)):
    print(thislist[i])

i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

---

## 6. List Comprehension

newlist = [x for x in fruits if "a" in x]

newlist = [x.upper() for x in fruits]

newlist = [x for x in range(10)]

Syntax:
newlist = [expression for item in iterable if condition]

---

## 7. Sorting Lists

list.sort(reverse=True, key=myFunc)

---

## 8. Copying Lists

mylist = thislist.copy()
mylist = list(thislist)
mylist = thislist[:]

---

## 9. Tuples (Immutable)

Tuples cannot be changed after creation.

Workaround:
- convert tuple → list → modify → convert back

Packing/unpacking:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

Tuple methods:
count()
index()

---

## 10. Sets

add()
remove()
discard()
union()
intersection()
difference()
clear()

---

## 11. Dictionaries

for x in thisdict:
    print(x)

for x in thisdict.values():
    print(x)

for x, y in thisdict.items():
    print(x, y)

Methods:
get(), keys(), values(), items(), pop(), update(), clear()

---

## 12. Condition Operators

==  equal
!=  not equal
<   less than
<=  less or equal
>   greater than
>=  greater or equal

---

## 13. Functions

Positional:
func("hello")

Keyword:
func(name="hello")

---

*args:
def my_function(*args):
    print(args)

**kwargs:
def my_function(**kwargs):
    print(kwargs)

Combined:
def my_function(title, *args, **kwargs):
    print(title)
    print(args)
    print(kwargs)

---

## 🎯 Summary

- Lists: mutable and flexible
- Tuples: immutable
- Sets: unique values + math operations
- Dictionaries: key-value storage
- Functions: support flexible arguments (*args, **kwargs)




# 📘 Python Day 2 — File Handling Report

## 1. Opening and Reading Files

Python allows reading files using `open()` and displaying content with `.read()`.

### Basic file read
f = open("File-Handling/week-01-Python-Report.txt")
print(f.read())
f.close()

- Opens a file in read mode (default)
- Reads full content of the file
- Must be manually closed using `close()`

---

### Using `with open()` (recommended)
with open("File-Handling/week-01-Python-Report.txt") as myFile:
    print(myFile.read())

- Automatically closes the file after execution
- No need to call `close()`

---

### Reading limited characters
with open("File-Handling/week-01-Python-Report.txt") as myFile:
    print(myFile.read(100))

- Reads only first 100 characters

---

## 2. Reading Line by Line

### Using readline()
f = open("File-Handling/week-01-Python-Report.txt")
print(f.readline())
print(f.readline())
f.close()

- Reads file line by line

---

### Looping through file
f = open("File-Handling/week-01-Python-Report.txt")
for x in f:
    print(x)
f.close()

- Efficient way to read all lines one by one

---

## 3. Writing to Files

### Append mode ("a")
with open("File-Handling/week-01-Python-Report.txt", "a") as myFile:
    myFile.write("Hello this line has been appended")

- Adds content at the end of file
- Does not overwrite existing content

---

### Write mode ("w")
with open("File-Handling/write-test.txt", "w") as myFile:
    myFile.write("This will overwrite existing content")

- Creates file if it doesn't exist
- Overwrites existing content

---

## 4. Creating Files

newFile = open("File-Handling/new-file.txt", "x")
newFile.close()

- `"x"` mode creates a new file
- Gives error if file already exists

---

## 5. Deleting Files and Folders

### Delete file
import os
os.remove("File-Handling/new-file.txt")

- Removes a specific file

---

### Delete folder
import os
os.rmdir("myfolder")

- Removes an empty folder only

---

## 🎯 Summary

- `open()` is used for file handling in Python
- `with open()` is preferred because it auto-closes files
- File modes:
  - `"r"` → read
  - `"a"` → append
  - `"w"` → write (overwrite)
  - `"x"` → create
- Always manage files carefully to avoid data loss
- `os` module is used for deleting files and directories
