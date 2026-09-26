'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập năm sản xuất rồi đề xuất sửa chữa
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
     # Nhập số năm và chuyển thành kiểu số nguyên
     nam_sx=int(input("Nhập năm sản xuất: "))
     # Nếu số năm từ 15 trở lên
     if nam_sx >= 15:
          # In đề xuất "Thay thế"
          print("Thay thế")
     # Nếu số năm từ 10 đến dưới 15
     elif nam_sx >= 10:
          # In đề xuất "Bao tri"
          print("Bao tri")
     # Nếu số năm nhỏ hơn 10
     else:
          # In ra "Không có đề xuất"
          print("Không có đề xuất")