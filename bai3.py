"""
I. PHÂN TÍCH INPUT / OUTPUT
Chức năng 1: Nhập dữ liệu đơn hàng
Input
sender_name      # str
sender_phone     # str
pickup_address   # str

receiver_name    # str
receiver_phone   # str
delivery_address # str

note             # str

Ví dụ:

sender_name = "  nguyen van a "
sender_phone = "0987654321"

pickup_address = "  123 nguyen trai q1 "

receiver_name = " tran thi b "
receiver_phone = "0971234532"

delivery_address = " 456 le loi q3 "

note = " giao hàng trước 18h "
Output
Tên người gửi: Nguyen Van A
Tên người nhận: Tran Thi B

Địa chỉ lấy hàng: 123 nguyen trai q1
Địa chỉ giao hàng: 456 le loi q3

Ghi chú: giao hàng trước 18h

Độ dài ghi chú: 20
Số từ trong ghi chú: 4

Ghi chú chữ thường:
giao hàng trước 18h

Ghi chú chữ hoa:
GIAO HÀNG TRƯỚC 18H
Chức năng 2: Chuẩn hóa mã đơn hàng
Input
gx 12345
Output
GRAB-GX-12345
Chức năng 3: Ẩn số điện thoại
Input
0987654321
Output
098*****21
Chức năng 4: Tìm kiếm & thay thế
Input
Từ khóa: giao
Thay thế: vận chuyển
Output
Số lần xuất hiện: 2

Ghi chú mới:
vận chuyển hàng trước 18h
II. ĐỀ XUẤT GIẢI PHÁP
Các hàm xử lý chuỗi cần dùng
Hàm	Chức năng
strip()	Xóa khoảng trắng đầu cuối
title()	Viết hoa chữ cái đầu từ
lower()	Chuyển thường
upper()	Chuyển hoa
split()	Tách chuỗi
replace()	Thay thế
count()	Đếm số lần xuất hiện
startswith()	Kiểm tra tiền tố
isdigit()	Kiểm tra toàn số
Biến lưu dữ liệu
sender_name = ""
sender_phone = ""

receiver_name = ""
receiver_phone = ""

pickup_address = ""
delivery_address = ""

note = ""

order_code = ""
Kiểm tra số điện thoại

Điều kiện:

phone.isdigit()

và

len(phone) == 10
Ẩn số điện thoại

Ví dụ:

0987654321

Tách:

phone[:3]

→

098

Tách cuối:

phone[-2:]

→

21

Ghép:

phone[:3] + "*" * 5 + phone[-2:]

Kết quả:

098*****21
III. PSEUDOCODE
Khai báo các biến lưu dữ liệu

while True

    Hiển thị menu

    Nhập lựa chọn

    Nếu nhập sai kiểu dữ liệu
        báo lỗi
        quay lại menu

    match choice

        case 1:
            nhập thông tin đơn hàng
            kiểm tra dữ liệu rỗng
            hiển thị báo cáo

        case 2:
            nhập mã đơn hàng
            chuẩn hóa mã

        case 3:
            kiểm tra số điện thoại
            ẩn số điện thoại

        case 4:
            tìm kiếm và thay thế

        case 5:
            thoát

        case _:
            báo lỗi
"""

# ==================================
# HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB
# ==================================

sender_name = ""
sender_phone = ""

receiver_name = ""
receiver_phone = ""

pickup_address = ""
delivery_address = ""

note = ""

while True:

    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG =====")
    print("1. Nhập dữ liệu đơn hàng")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại")
    print("4. Tìm kiếm và thay thế từ khóa")
    print("5. Thoát")

    try:
        choice = int(input("Nhập lựa chọn: "))
    except ValueError:
        print("Lựa chọn không hợp lệ")
        continue

    match choice:

        # =====================
        # CHỨC NĂNG 1
        # =====================
        case 1:

            sender_name = input("Tên người gửi: ")
            sender_phone = input("SĐT người gửi: ")
            pickup_address = input("Địa chỉ lấy hàng: ")

            receiver_name = input("Tên người nhận: ")
            receiver_phone = input("SĐT người nhận: ")
            delivery_address = input("Địa chỉ giao hàng: ")

            note = input("Ghi chú giao hàng: ")

            fields = {
                "Tên người gửi": sender_name,
                "SĐT người gửi": sender_phone,
                "Địa chỉ lấy hàng": pickup_address,
                "Tên người nhận": receiver_name,
                "SĐT người nhận": receiver_phone,
                "Địa chỉ giao hàng": delivery_address,
                "Ghi chú giao hàng": note
            }

            has_error = False

            for field_name, value in fields.items():
                if value.strip() == "":
                    print(f"{field_name} không được bỏ trống")
                    has_error = True

            if has_error:
                continue

            sender_name = sender_name.strip().title()
            receiver_name = receiver_name.strip().title()

            pickup_address = pickup_address.strip()
            delivery_address = delivery_address.strip()

            note = note.strip()

            print("\n===== BÁO CÁO =====")

            print("Tên người gửi:", sender_name)
            print("Tên người nhận:", receiver_name)

            print("Địa chỉ lấy hàng:", pickup_address)
            print("Địa chỉ giao hàng:", delivery_address)

            print("Ghi chú:", note)

            print("Độ dài ghi chú:", len(note))
            print("Số lượng từ:", len(note.split()))

            print("\nGhi chú chữ thường:")
            print(note.lower())

            print("\nGhi chú chữ hoa:")
            print(note.upper())

        # =====================
        # CHỨC NĂNG 2
        # =====================
        case 2:

            order_code = input(
                "Nhập mã đơn hàng: "
            )

            if order_code.strip() == "":
                print("Mã đơn hàng không được bỏ trống")
                continue

            print("Mã ban đầu:", order_code)

            order_code = order_code.strip()
            order_code = order_code.upper()

            order_code = order_code.replace(
                " ",
                "-"
            )

            if not order_code.startswith(
                "GRAB-"
            ):
                order_code = (
                    "GRAB-" + order_code
                )

            print(
                "Mã sau chuẩn hóa:",
                order_code
            )

        # =====================
        # CHỨC NĂNG 3
        # =====================
        case 3:

            if sender_phone == "" or receiver_phone == "":
                print(
                    "Chưa có dữ liệu số điện thoại"
                )
                continue

            phones = [
                ("Người gửi", sender_phone),
                ("Người nhận", receiver_phone)
            ]

            for owner, phone in phones:

                if not phone.isdigit():
                    print(
                        f"Số điện thoại {owner} không hợp lệ"
                    )
                    continue

                if len(phone) != 10:
                    print(
                        f"Số điện thoại {owner} không hợp lệ: Số điện thoại phải có đúng 10 ký tự"
                    )
                    continue

                hidden_phone = (
                    phone[:3]
                    + "*" * 5
                    + phone[-2:]
                )

                print(
                    f"SĐT {owner}:",
                    hidden_phone
                )

        # =====================
        # CHỨC NĂNG 4
        # =====================
        case 4:

            if note == "":
                print(
                    "Chưa có ghi chú giao hàng để tìm kiếm"
                )
                continue

            old_keyword = input(
                "Từ khóa cần tìm: "
            )

            new_keyword = input(
                "Từ khóa thay thế: "
            )

            count = note.count(
                old_keyword
            )

            if count > 0:

                note = note.replace(
                    old_keyword,
                    new_keyword
                )

                print(
                    "\nSố lần xuất hiện:",
                    count
                )

                print(
                    "\nGhi chú sau khi thay thế:"
                )

                print(note)

            else:
                print(
                    "Không tìm thấy từ khóa trong ghi chú."
                )

        # =====================
        # CHỨC NĂNG 5
        # =====================
        case 5:
            print("Thoát chương trình")
            break

        # =====================
        # MENU SAI
        # =====================
        case _:
            print(
                "Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5."
            )
