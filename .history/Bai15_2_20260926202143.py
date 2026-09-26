'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: In các số từ 99 đến 1 mà chia hết cho 7
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
     # Duyệt biến i đếm lùi từ 99 về 1
     for i in range(99, 1-1, -1):
          # Nếu i chia hết cho 7 (dư 0) thì in i ra cách nhau bằng khoảng trắng
          if i%7==0: print(i, end=" ")