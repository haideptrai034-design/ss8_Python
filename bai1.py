"""
1. PHÂN TÍCH & THIẾT KẾ
1.1. Input / Output
Chức năng 1: Nhập dữ liệu và thống kê
Input
username (str)
title (str)
description (str)
hashtags (str)

Ví dụ:

username = "  Rikkei Education  "
title = "  hoc python co ban "
description = "  Python la ngon ngu lap trinh pho bien "
hashtags = "#python, #coding, #learnpython"
Output
Tên tài khoản: Rikkei Education
Tiêu đề: Hoc Python Co Ban
Mô tả: Python la ngon ngu lap trinh pho bien

Độ dài mô tả: 35
Số từ: 7

Hashtag:
#python
#coding
#learnpython

Số lượng hashtag: 3

Mô tả viết thường:
python la ngon ngu lap trinh pho bien

Mô tả viết hoa:
PYTHON LA NGON NGU LAP TRINH PHO BIEN
Chức năng 2: Chuẩn hóa tài khoản
Input
Rikkei Education
Output
@rikkei education
Chức năng 3: Kiểm tra hashtag
Input
#python
Output
Hashtag hợp lệ
Đã thêm vào danh sách hashtag
Chức năng 4: Tìm kiếm và thay thế
Input
Từ khóa cần tìm:
python

Từ khóa thay thế:
java
Output
Số lần xuất hiện: 2

Mô tả mới:
java là ngôn ngữ lập trình...
1.2. Các phương thức String cần dùng
Phương thức	Công dụng
strip()	Xóa khoảng trắng đầu cuối
title()	Viết hoa chữ cái đầu mỗi từ
lower()	Chuyển thành chữ thường
upper()	Chuyển thành chữ hoa
split()	Tách chuỗi
replace()	Thay thế chuỗi
count()	Đếm số lần xuất hiện
startswith()	Kiểm tra bắt đầu bằng ký tự
isalnum()	Kiểm tra chữ và số
1.3. Giải pháp
Lưu dữ liệu video
username = ""
title = ""
description = ""
hashtags = []
Chuẩn hóa hashtag

Người dùng nhập:

"#python, #coding, #learnpython"

Tách:

hashtags = hashtags_input.split(",")

Loại bỏ khoảng trắng:

hashtags = [tag.strip() for tag in hashtags]
Kiểm tra hashtag hợp lệ

Điều kiện:

# Không rỗng

# Bắt đầu bằng #

# Không có khoảng trắng

# Độ dài >= 2

# Chỉ chứa:
a-z
A-Z
0-9
_

Ví dụ:

#python

Hợp lệ

Ví dụ:

#hoc python

Không hợp lệ vì có khoảng trắng.

Kiểm tra menu

Dùng:

try:
    choice = int(input())
except:

để xử lý:

abc
@
2.5
1.4. Pseudocode
Khai báo dữ liệu video

Lặp vô hạn

    Hiển thị menu

    Nhập lựa chọn

    Nếu nhập sai kiểu dữ liệu
        Thông báo lỗi
        Quay lại menu

    Nếu chọn 1
        Nhập dữ liệu video
        Kiểm tra username
        Kiểm tra description
        Thống kê dữ liệu

    Nếu chọn 2
        Chuẩn hóa username

    Nếu chọn 3
        Nhập hashtag
        Kiểm tra hợp lệ
        Nếu hợp lệ
            Thêm vào danh sách

    Nếu chọn 4
        Tìm kiếm từ khóa
        Nếu tồn tại
            thay thế
        Ngược lại
            thông báo

    Nếu chọn 5
        Thoát

    Nếu khác 1-5
        Báo lỗi
2. SOURCE CODE HOÀN CHỈNH
"""

while True:
    print("+==========================================+")
    print("    hệ thống quản lý nội dung tiktok    ")
    print("1. Nhập và phân tích thông tin vide0")
    print("2. chuẩn hóa tên tài tài khoản")
    print("3. kiểm tra hagstah hợp lệ")
    print("4. tìm kiếm và thay thế từ khóa")
    print("5. Thoát chương trình")
    print("+==========================================+")

    choice = int(input(">Mời bạn chọn chức năng (1-5): "))

    match (choice):
        case 1:
            print("Nhập và phân tích video")
            user_name = input("Nhập tên tài khoản: ")
            title = input("Nhập tiêu đề video: ")
            descripstion = input("Nhập mô tả video: ")
            list_hashtag = input("Nhập danh sách hasgtash (cách nhau dấu ,): ")
            print("đã qua xử lí")
            print(f"Tên tài khoản: {user_name.strip}")
            print(f"Tiêu đề video {title.title().strip()}")
            print(f"Mô tả {descripstion.strip()}")
            print(f"Độ dài mô tả {len(descripstion)}")
            count_space = descripstion.count(" ") + 1
            print(f"Số lượng từ trong mô tả: {count_space}")
            listhasgtag_ = list_hashtag.split(",")
            new_listhasgtag = "".join(listhasgtag_)
            print(f"Danh sách hasgtag: {new_listhasgtag}")
            cuont_hasgtag = len(listhasgtag_)
            print(f"Số lượng hasgtag: {cuont_hasgtag}")
            print(f"Mô tả video thành thường {descripstion.lower()}")
            print(f"Mô tả video thành hoa {descripstion.upper()}")
        case 2:
            print(f"Mô tả trước khi chuyển hóa: {user_name}")
            print(f"tên tài khoản sau khi chuyển hóa {"@" + user_name.lower()}")

        case 3:
            hashtag = input("Nhập hashtag: ")
            if (hashtag == ""):
                print("Không được rỗng")
            elif (not hashtag.startswith("#")):
                print("Phải bắt đầu bằng dấu #")
            elif (" " in hashtag):
                print("Hashtag không được chứa khoảng trắng")
            elif (len(hashtag) < 2):
                print("phải chứa tối thiểu 2 ký tự")
            else:
                print("Hợp lệ")
                list_hashtag = list_hashtag + hashtag
                print(f'Danh sách hashtag mới: {list_hashtag}')
        case 4:
            find_word = print('Nhập từ khóa cần tìm: ')
            count_word = descripstion.count(find_word)
            if(count_word > 0):
               descripstion=  descripstion.replace(find_word,"từ khóa mới")
               print(f"{descripstion}")
               print("só lần xuất hiện từ khóa: {count_word}")
            else:
                print("Từ khóa không tìm thấy")
        case 5:
            print("Thoát chương trình")
            break
        case _:
            print("Lựa chọn không hợp lệ:")
