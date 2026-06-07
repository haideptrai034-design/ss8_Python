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

username = ""
title = ""
description = ""
hashtags = []

while True:
    print("\n+==========================================+")
    print("      HỆ THỐNG QUẢN LÝ NỘI DUNG TIKTOK")
    print("1. Nhập và phân tích thông tin video")
    print("2. Chuẩn hóa tên tài khoản")
    print("3. Kiểm tra hashtag hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát chương trình")
    print("+==========================================+")

    try:
        choice = int(input("Mời bạn chọn chức năng (1-5): "))
    except:
        print("Vui lòng nhập số từ 1-5!")
        continue

    match choice:
        case 1:
            print("\n===== NHẬP THÔNG TIN VIDEO =====")

            username = input("Nhập tên tài khoản: ")
            title = input("Nhập tiêu đề video: ")
            description = input("Nhập mô tả video: ")
            hashtags_input = input("Nhập hashtag (cách nhau bởi dấu ,): ")

            # Xử lý dữ liệu
            username = username.strip()
            title = title.strip().title()
            description = description.strip()

            hashtags = hashtags_input.split(",")

            print("\n===== THÔNG TIN SAU XỬ LÝ =====")
            print(f"Tên tài khoản: {username}")
            print(f"Tiêu đề: {title}")
            print(f"Mô tả: {description}")

            print(f"\nĐộ dài mô tả: {len(description)}")
            print(f"Số từ: {len(description.split())}")

            print("\nHashtag:")
            for tag in hashtags:
                print(tag.strip())

            print(f"\nSố lượng hashtag: {len(hashtags)}")

            print("\nMô tả viết thường:")
            print(description.lower())

            print("\nMô tả viết hoa:")
            print(description.upper())

        case 2:
            if username == "":
                print("Bạn chưa nhập dữ liệu video!")
            else:
                print(f"Tên tài khoản sau chuẩn hóa: @{username.lower()}")

        case 3:
            hashtag = input("Nhập hashtag cần kiểm tra: ").strip()

            if hashtag == "":
                print("Hashtag không được để trống!")

            elif not hashtag.startswith("#"):
                print("Hashtag phải bắt đầu bằng dấu #")

            elif " " in hashtag:
                print("Hashtag không được chứa khoảng trắng")

            elif len(hashtag) < 2:
                print("Hashtag phải có ít nhất 2 ký tự")

            else:
                noi_dung = hashtag[1:]

                if noi_dung.replace("_", "").isalnum():
                    print("Hashtag hợp lệ")

                    hashtags.append(hashtag)

                    print("Đã thêm vào danh sách hashtag")
                else:
                    print("Hashtag không hợp lệ")

        case 4:
            if description == "":
                print("Bạn chưa nhập mô tả!")
            else:
                find_word = input("Nhập từ khóa cần tìm: ")
                replace_word = input("Nhập từ khóa thay thế: ")

                count_word = description.lower().count(find_word.lower())

                if count_word > 0:
                    description = description.replace(
                        find_word,
                        replace_word
                    )

                    print(f"\nSố lần xuất hiện: {count_word}")

                    print("\nMô tả mới:")
                    print(description)

                else:
                    print("Không tìm thấy từ khóa!")

        case 5:
            print("Thoát chương trình!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")
