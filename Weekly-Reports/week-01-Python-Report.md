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
