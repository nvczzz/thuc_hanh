'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập điểm rồi xét học bổng
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
     # Nhập điểm từ bàn phím và ép kiểu về số thực
     diem=float(input("Nhập điểm: "))
     # Điểm từ 9 trở lên
     if diem >= 9:
          # In mức học bổng 5,000,000
          print(5000000)
     # Điểm từ 8 đến dưới 9
     elif diem >= 8:
          # In mức học bổng 3,000,000
          print(3000000)
     # Điểm từ 7 đến dưới 8
     elif diem >= 7:
          # In mức học bổng 1,000,000
          print(1000000)
     # Điểm dưới 7
     else:
          # In mức học bổng 0
          print(0)