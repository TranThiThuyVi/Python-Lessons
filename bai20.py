"""
12/16/2022 
Vi
"""
#in kiểu dữ liệu
a = 10
print(type(a))
b = 10.5
print(type(b))
c = True
print(type(c))
d = "Hola"
print(type(d))

#Cộng chuỗi
s1 = "Hola"
s2 = "Mucho gusto"
s3 = s1 + " " + s2
print(s3)

#tạo chuỗi nhiều dòng
chuoiNhieuDong = '''
Hola
Yo soy Vi
Mucho gusto
'''

#lặp lại chuỗi
ghiNho = "Em hứa sẽ cố gắng chăm học hơn \n"
ghiNho_10 = ghiNho * 10
print(ghiNho_10)

#Kiểm tra chuỗi có thuộc chuỗi khác
chuoi_1 = "Hola Mucho gusto"
chuoi_2 = "yo soy Vi"
chuoi_3 = "Mucho gusto"

if chuoi_2 in chuoi_1:
    print("chuỗi 2 là chuỗi con của chuỗi một")
else:
    print("chuỗi 2 không là chuỗi con của chuỗi một")

if chuoi_3 in chuoi_1:
    print("chuỗi 3 là chuỗi con của chuỗi một")
else:
    print("chuỗi 3 không là chuỗi con của chuỗi một")

#viết hoa chữ đầu của chuỗi
s = "una camiseta verde y un carro azul"
s = str.capitalize(s)
print(s)

#Viết hoa toàn bộ chuỗi
s = s.upper()
print(s)

#Viết thường toàn bộ chuỗi
s = s.lower()
print(s)

#Tìm và đếm số lượng chuỗi con
s = "Lập trinh Python là xu hướng hiện nay. Bạn nên học lập trình Python"
print(s.find("PythonX"))#trả về -1 nếu không tìm thấy, ngược lại trả về vị trí đầu tiên
print(s.find("Python"))

print(s.count("Python"))

#thay thế chuỗi
s = "Lập trinh Python là xu hướng hiện nay. Bạn nên học lập trình Python"
s = s.replace("Python", "PYTHON")
print(s)

#Cắt chuỗi thành 1 list
s = "Lập trinh Python là xu hướng hiện nay. Bạn nên học lập trình Python"
list1 = s.split(" ")
print(list1)

list2 = s.split(".")
print(list2)

#format
print("{0} + {1} = {2}".format(1, 2, 1 + 2))

#lấy chuỗi con
print(s[0:10])
