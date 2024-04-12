"""
12/116/2022 
Vi
"""
#tạo list rỗng
emptyList = []

#Tạo ra một đối tượng list
emptyList1 = list()

print(emptyList)
print(emptyList1)

#Tạo ra list có dữ liệu
colors = ["red", "green", "orange", 1, 2]
print(colors)

#List có thứ tự, vị trí các phần tử được đánh dấu từ 0, từ trái sang phải
studentList = ["An", "Bình", "Ngân", "Vy"]
print(studentList[2])
print(studentList[0])
print(studentList)
print(studentList[:])

#studentList[x:y] => lấy ra [x:y]
print(studentList[1:2])
print(studentList[0:2])
print(studentList[1:4])

#thêm phần tử vào cuối List
studentList.append("Thiên")
print(studentList)

studentList[len(studentList):] = ["Thành"]
print(studentList)

#Chèn phần tử vào List
studentList.insert(2, "Ngọc")
print(studentList)

#Số lượng phần tử có trong List: => len
print(len(studentList))

#Đếm số phần tử thỏa điều kiện 
print("Đếm Ngọc: ", studentList.count("Ngọc"))
print("Đếm Thành: ", studentList.count("Thành"))
print("Đếm An: ", studentList.count("An"))

#Kiểm tra phần tử có trong list: in
#Xóa phần tử ra khỏi list bằng giá trị

if "Ngọc" in studentList:
    studentList.remove("Ngọc")
    print(studentList)

#Xóa phần tử ra khỏi list bằng vị trí
studentList.pop(0)
print(studentList)

#Đảo ngược list
studentList.reverse()
print(studentList)

#Sắp xếp list
studentList.sort()
print(studentList)

numbers = [7, 5, 1, 9, 0, 5, 7]
numbers.sort()
print(numbers)

#Sắp xếp ngược
studentList.sort(reverse=True)
print(studentList)
numbers.sort(reverse=True)
print(numbers)

#Xóa sạch dữ liệu trong list
studentList.clear()
print(studentList)
