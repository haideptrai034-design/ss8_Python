"""
I. PHÂN TÍCH INPUT / OUTPUT
Chức năng 1: Nhập dữ liệu sản phẩm
Input
shop_name      # str
product_name   # str
description    # str
category       # str
keywords       # str

Ví dụ:

shop_name = " Rikkei Education Mall "
product_name = " tai nghe bluetooth "
description = " Tai nghe bluetooth âm thanh tốt, pin lâu "
category = " Điện Tử "
keywords = "bluetooth, tai nghe, âm thanh"
Output
Tên shop: Rikkei Education Mall
Tên sản phẩm: Tai Nghe Bluetooth
Mô tả: Tai nghe bluetooth âm thanh tốt, pin lâu

Độ dài mô tả: 39

Danh mục: điện tử

Danh sách từ khóa:
bluetooth
tai nghe
âm thanh

Số lượng từ khóa: 3

Mô tả viết thường:
tai nghe bluetooth âm thanh tốt, pin lâu

Mô tả viết hoa:
TAI NGHE BLUETOOTH ÂM THANH TỐT, PIN LÂU
Chức năng 2: Chuẩn hóa tên shop
Input
" Rikkei Education Mall "
Output
shop-rikkei-education-mall
Chức năng 3: Kiểm tra mã giảm giá
Input
SALE2025
Output
Mã giảm giá hợp lệ
Danh sách mã giảm giá:

SALE2025
Chức năng 4: Tìm kiếm và thay thế
Input
âm thanh
chất âm
Output
Số lần xuất hiện: 2

Tai nghe bluetooth chất âm tốt,
pin lâu, chất âm rõ ràng
II. GIẢI PHÁP
Các hàm xử lý chuỗi cần dùng
Hàm	Công dụng
strip()	Xóa khoảng trắng đầu cuối
title()	Viết hoa chữ cái đầu từ
lower()	Chuyển thường
upper()	Chuyển hoa
replace()	Thay thế
split()	Tách chuỗi
count()	Đếm số lần xuất hiện
startswith()	Kiểm tra bắt đầu bằng SALE
isupper()	Kiểm tra viết hoa
isalnum()	Chỉ chứa chữ và số
Cấu trúc dữ liệu
shop_name = ""
product_name = ""
description = ""
category = ""

keyword_list = []

discount_codes = []
III. PSEUDOCODE
Khai báo biến lưu dữ liệu

Lặp vô hạn

    Hiển thị menu

    Nhập lựa chọn

    Nếu nhập sai kiểu dữ liệu
        báo lỗi
        quay lại menu

    match choice

        case 1:
            nhập dữ liệu
            kiểm tra tên shop
            kiểm tra mô tả
            thống kê dữ liệu

        case 2:
            chuẩn hóa tên shop

        case 3:
            kiểm tra mã giảm giá

        case 4:
            tìm kiếm và thay thế

        case 5:
            thoát chương trình

        case _:
            báo lựa chọn không hợp lệ
IV. CODE HOÀN CHỈNH (DÙNG MATCH CASE)
"""
# ==================================
# HỆ THỐNG KIỂM DUYỆT SẢN PHẨM SHOPEE
# ==================================

shop_name = ""
product_name = ""
description = ""
category = ""

keyword_list = []
discount_codes = []

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ SẢN PHẨM =====")
    print("1. Nhập dữ liệu sản phẩm")
    print("2. Chuẩn hóa tên shop")
    print("3. Kiểm tra mã giảm giá")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát")

    try:
        choice = int(input("Nhập lựa chọn: "))
    except ValueError:
        print("Lựa chọn không hợp lệ!")
        continue

    match choice:

        # =====================
        # CHỨC NĂNG 1
        # =====================
        case 1:

            shop_name = input("Tên shop: ")
            product_name = input("Tên sản phẩm: ")
            description = input("Mô tả sản phẩm: ")
            category = input("Danh mục sản phẩm: ")

            keywords = input(
                "Danh sách từ khóa (cách nhau bởi dấu phẩy): "
            )

            if shop_name.strip() == "":
                print("Tên shop không được bỏ trống")
                continue

            if description.strip() == "":
                print("Mô tả sản phẩm không được rỗng")
                continue

            shop_name = shop_name.strip()
            product_name = product_name.strip().title()
            description = description.strip()
            category = category.strip().lower()

            keyword_list = keywords.split(",")

            for i in range(len(keyword_list)):
                keyword_list[i] = keyword_list[i].strip()

            print("\n===== BÁO CÁO THỐNG KÊ =====")

            print("Tên shop:", shop_name)
            print("Tên sản phẩm:", product_name)
            print("Mô tả:", description)

            print(
                "Độ dài mô tả:",
                len(description)
            )

            print("Danh mục:", category)

            print("\nDanh sách từ khóa:")

            for keyword in keyword_list:
                print("-", keyword)

            print(
                "\nSố lượng từ khóa:",
                len(keyword_list)
            )

            print("\nMô tả viết thường:")
            print(description.lower())

            print("\nMô tả viết hoa:")
            print(description.upper())

        # =====================
        # CHỨC NĂNG 2
        # =====================
        case 2:

            if shop_name == "":
                print("Chưa có dữ liệu shop.")
                continue

            print("Tên shop ban đầu:")
            print(shop_name)

            normalized_shop = (
                shop_name.strip()
                .lower()
                .replace(" ", "-")
            )

            if not normalized_shop.startswith("shop-"):
                normalized_shop = (
                    "shop-" + normalized_shop
                )

            print("Tên shop chuẩn hóa:")
            print(normalized_shop)

        # =====================
        # CHỨC NĂNG 3
        # =====================
        case 3:

            code = input(
                "Nhập mã giảm giá: "
            ).strip()

            if code == "":
                print("Mã giảm giá không được rỗng")

            elif " " in code:
                print("Mã giảm giá không được chứa khoảng trắng")

            elif len(code) < 6 or len(code) > 12:
                print(
                    "Mã giảm giá phải có độ dài từ 6 đến 12 ký tự"
                )

            elif not code.isupper():
                print(
                    "Mã giảm giá phải viết hoa toàn bộ"
                )

            elif not code.isalnum():
                print(
                    "Mã giảm giá chỉ được chứa chữ cái và chữ số"
                )

            elif not code.startswith("SALE"):
                print(
                    "Mã giảm giá phải bắt đầu bằng SALE"
                )

            else:

                discount_codes.append(code)

                print("Mã giảm giá hợp lệ")

                print("\nDanh sách mã giảm giá:")

                for item in discount_codes:
                    print(item)

        # =====================
        # CHỨC NĂNG 4
        # =====================
        case 4:

            if description == "":
                print(
                    "Chưa có mô tả sản phẩm."
                )
                continue

            old_keyword = input(
                "Từ khóa cần tìm: "
            )

            new_keyword = input(
                "Từ khóa thay thế: "
            )

            count = description.count(
                old_keyword
            )

            if count > 0:

                description = description.replace(
                    old_keyword,
                    new_keyword
                )

                print(
                    "\nSố lần xuất hiện của từ khóa:",
                    count
                )

                print(
                    "\nMô tả sau khi thay thế:"
                )
                print(description)

            else:
                print(
                    "Không tìm thấy từ khóa trong mô tả."
                )

        # =====================
        # CHỨC NĂNG 5
        # =====================
        case 5:
            print("Thoát chương trình")
            break

        # =====================
        # MENU KHÔNG HỢP LỆ
        # =====================
        case _:
            print(
                "Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5."
            )