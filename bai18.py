"""
12/116/2022 
Vi
"""

#Vòng lặp đi từ 0 đến < n, mỗi lần tăng lên một đơn vị
n = 10
for i in range(n):
    print(i)

#Ví dụ tính tổng từ 0 -> n
n = int(input("Nhập vào n:"))
tong = 0
for i in range(n + 1):
    tong += i
print("Tổng = ", tong)

#Vòng lặp for có bước tăng tùy chỉnh
for i in range(0, 10, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

colors = ["red", "green", "orange"]

#Vòng lặp for duyệt các phần tử của list
for color in colors:
    print(color)

#Vòng lâp for duyệt phần tử theo vị trí
for i in range(len(colors)):
    print(colors[i])
