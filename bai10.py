"""
12/14/2022 
Vi
"""

print("Toán tử so sánh: ")
x = int(input("x: "))
y = int(input("y: "))

#True or False
print("{0} < {1} la {2}".format(x, y, x < y))
print("{0} > {1} la {2}".format(x, y, x > y))
print("{0} == {1} la {2}".format(x, y, x == y))
print("{0} != {1} la {2}".format(x, y, x != y))
print("{0} <= {1} la {2}".format(x, y, x <= y))
print("{0} >= {1} la {2}".format(x, y, x >= y))

print("Toán tử logic")
z = int(input("z: "))

# and: toàn true => true, 1 true 1 false =>false, toàn false => false
print("({0} < {1}) and ({2} < {3}) = {4}".format(x, y, y, z, (x < y) and (y < z)))

#or chỉ cần 1 true => true
print("({0} < {1}) or ({2} < {3}) = {4}".format(x, y, y, z, (x < y) or (y < z)))
print(" not ({0} > {1}) = {2}".format(x, z, not (x > z)))