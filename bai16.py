"""
12/15/2022 
Vi
"""
"""
Nhập 3 điểm trên hệ trục tọa độ Oxy
1. Xác định 3 điểm có tạo thành tam giác không?
2. Nếu tạo thành tam giác:
    2.a Xuất ra chu vi của tam giác
    2.b Xuất ra diện tích của tam giác
"""

import math

#nhập dữ liệu
xA = float(input("Nhập xA: "))
yA = float(input("Nhập yA: "))
xB = float(input("Nhập xB: "))
yB = float(input("Nhập yB: "))
xC = float(input("Nhập xC: "))
yC = float(input("Nhập yC: "))

#Tính các cạnh của tam giác
AB = math.sqrt((xB - xA) ** 2 + (yB - yA)**2)
BC = math.sqrt((xC - xB) ** 2 + (yC - yB)**2)
AC = math.sqrt((xC - xA) ** 2 + (yC - yA)**2)

#Kiểm tra
if(AB + BC > AC) and (AB + AC > BC) and (BC + AC > AB):
    print("Tạo thành một tam giác")

    #Tính chu vi
    cv = AB + BC + AC
    print("Chu vi cua tam giác là: ", cv)

    #Tính diện tích
    p = cv / 2
    s = math.sqrt(p*(p - AB)*(p - BC)*(p - AC))
    print("Chu vi của tam giác là: ", s)
else:
    print("Không tạo thành tam giác")