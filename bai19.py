"""
12/16/2022 
Vi
"""

#Bảng cửu chương 2
for i in range(1, 11):
    print("2 x {0} = {1}".format(i, 2*i))


#in bảng cửu chương từ 2 đến 9
for j in range(2, 10):
    print("\nBảng cửu chương ", j)
    for i in range(1, 11):
        print("{0} x {1} = {2}".format(j, i, j*i))
