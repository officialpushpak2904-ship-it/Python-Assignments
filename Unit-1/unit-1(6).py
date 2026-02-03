myset = ("apple", "banana", "cherry")
print(type(myset))

thisset = set(("apple", "banana", "cherry")) 
print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)


thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
fruits = {"pineapple", "mango", "papaya"}
thisset.update(fruits)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.remove("apple")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

