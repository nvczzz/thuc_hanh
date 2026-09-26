'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 số đến khi thoả mãn điều kiện: 0 < n < 100
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
     # lặp vô hạn
     # Tạo vòng lặp lặp lại liên tục
     while True:
          # Nhập số n từ bàn phím và ép kiểu thành số nguyên
          n=int(input("Nhập số trong khoảng từ 0 đến 100: "))
          # trong khoảng 0 đến 100 thì dừng rồi in ra
          # Kiểm tra n nằm trong khoảng (0, 100) thì thoát khỏi vòng lặp ngay lập tức
          if 0 < n < 100: break
     # In kết quả số n hợp lệ đã nhập
     print("=> Số bạn nhập là:", n)