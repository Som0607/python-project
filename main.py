print("hello world")
a = 5
print(id(a))
print(type(a), "\n")

# tuple is immutable,
# insertion order is preserved and duplicates allow
print("Tuple :")
tupp = (1, 2, "hello world", 3, 4, 4)
print(tupp)
print(type(tupp), "\n")

# Range datatype: Sequence of number and immutable
# print("Range : ")
range(10)  # 0 to 9
range(1, 10)  # 1 to 9
range(1, 15, 2)

# Set datatype : order is not preserved and duplicates are not aloud
# not support indexing
# Mutable in nature but Frozenset are ImMutable
print("Set :")
st = {1,2,3,4,"hello"}
print(st)
print(type(st), "\n")

# Conversion
print("Conversion :")
bn = bin(15)  # base to binary
print(bn)
oc = oct(15)  # base to octal
print(oc)
hx = hex(15)  # base to hexa
print(hx, "\n")

# String
print("String :")
str1 = '''Hello  
World
hii
bro'''
print(str1)

str2 = 'Hello World'
print(str2[:])
print(str2 * 3, "\n")
