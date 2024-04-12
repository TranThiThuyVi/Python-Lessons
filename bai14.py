"""
12/15/2022 
Vi
"""

#Câu lệnh điều kiện

x = input("Nhập vào số nguyên: ")
x = int(x)

#Dạng 1
if x > 0:
    print(x, "là số dương")

#dạng 2
if x % 2 == 0:
    print(x, "là số chẵn")
else:
    print(x, "là số lẻ")

#Dạng 3
if x >= 9:
    print("Xếp loại Xuất sắc")
elif x >= 8:
    print("Xếp loại Giỏi")
elif x >= 7:
    print("Xếp loại Khá")
elif x >= 5:
    print("Xếp loại Trung bình")
else:
    print("Xếp loại Yếu")
