"""
12/15/2022 
Vi
"""

x = input("Nhập vào số nguyên: ")
x = int(x)

kq = "Chẵn" if (x % 2 == 0) else "Lẻ"

print(x, "là số", kq)