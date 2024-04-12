"""
12/15/2022 
Vi
"""
import math

#Giải PT bậc 2

print("PT bậc 2 ax^2 + bx + c = 0")

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

print("\n PT là {0}x^2 + {1}x + {2} = 0".format(a, b, c))

#Xử lý
if (a!=0): 
    delta = b**2 - 4*a*c
    if (delta<0):
        print("\nPT vô nghiệm")
    elif (delta==0):
        x = -b/(2*a)
        print("\nPT co nghiệm kép x1 = x2 = ", x)
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("\nPT có 2 nghiệm phân biệt x1 = {0} và x2 = {1}".format(x1, x2))
else:
    print("\nKhông phải PT bặc 2")
