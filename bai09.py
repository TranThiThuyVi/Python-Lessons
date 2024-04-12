"""
12/14/2022 
Vi
"""
#Phải ép về kiểu số vì nhập từ bàn phím vào đều là kiểu str
a = input("Nhap vao a: ")
a = float(a)

b = input("Nhap vao b: ")
b = float(b)

print("{0} + {1} = {2}".format(a, b, a + b))
print("{0} - {1} = {2}".format(a, b, a - b))
print("{0} * {1} = {2}".format(a, b, a * b))
print("{0} / {1} = {2}".format(a, b, a / b))

#chia lấy dư 
print("{0} % {1} = {2}".format(a, b, a % b))

#Mũ
print("{0} ** {1} = {2}".format(a, b, a ** b))

#chia lấy phần nguyên
print("{0} // {1} = {2}".format(a, b, a // b))