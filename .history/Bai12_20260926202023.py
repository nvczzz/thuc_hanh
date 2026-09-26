'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập tuổi rồi kết luận lứa tuổi
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
     # Nhập tuổi từ bàn phím và ép kiểu về số nguyên
     age=int(input("Nhập tuổi: "))
     # Lớn hơn 50 tuổi
     if age > 50:
          # Kết luận "Cao niên"
          print("Cao niên")
     # Từ 40 đến 50 tuổi
     elif age > 39:
          # Kết luận "Trung niên"
          print("Trung niên")
     # Từ 18 đến 39 tuổi
     elif age > 17:
          # Kết luận "Thanh niên"
          print("Thanh niên")
     # Từ 11 đến 17 tuổi
     elif age > 10:
          # Kết luận "Vị thành niên"
          print("Vị thành niên")
     # Từ 3 đến 10 tuổi
     elif age > 2:
          # Kết luận "Nhi đồng"
          print("Nhi đồng")
     # Từ 2 tuổi trở xuống
     else:
          # Kết luận "Trẻ sơ sinh"
          print("Trẻ sơ sinh")