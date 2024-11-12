# In programming, data type is an important concept.
#
# Variables can store data of different types, and different types can do different things.
#
# Python has the following data types built-in by default, in these categories:
#
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType
from pandas.core.interchange.utils import dtype_to_arrow_c_fmt
from pywin.mfc.dialog import PrintDialog

a = "Hello World"
b = 20
c = 20.5
d = 1j
e = ["apple", "banana", "cherry"]
f = ("apple", "banana", "cherry")
g = range(6)
h = {"name" : "John", "age" : 36}
i = {"apple", "banana", "cherry"}
j = frozenset({"apple", "banana", "cherry"})
k = True
l = b"Hello"
m = bytearray(5)
n = memoryview(bytes(5))
o = None

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))
print(type(k))
print(type(l))
print(type(m))
print(type(o))
print(type(n))



# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
#
# 1.List is a collection which is ordered and changeable. Allows duplicate members.
# 2.Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# 3.Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# 4.Dictionary is a collection which is ordered** and changeable. No duplicate members.

# Examples
mylist = ["apple", "banana", "cherry"]
mytuple = ("apple", "banana", "cherry")
myset = {"apple", "banana", "cherry"}
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(mylist)
print(mytuple)
print(myset)
print(thisdict)