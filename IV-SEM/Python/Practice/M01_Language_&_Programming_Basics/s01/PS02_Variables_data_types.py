'''
Data Types :
1.Fundamental DT:
    1.int
    2.float
    3.complex
    4.boolean
    5.string
2.Collection DT:
    1.list
    2.tuple
    3.set
    4.dictionary
'''
x = 9
y = 9.9
z = 1 + 8j

print(z,type(z))
print(x + y)

c1 = 9 + 0j
c2 = complex(2,-3)
print(c2)
print(c1 + c2)
print(c1 - c2)
print(c1 / c2)
print(c1 * c2)

print(c1.real)
print(c1.imag)

j = "harsha"
print(j[::2])
print(j[::-1])