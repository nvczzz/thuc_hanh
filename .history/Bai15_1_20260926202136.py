'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: In các số từ 1 đến 100 mà chia hết cho 3
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
     # Duyệt biến i chạy từ 1 đến 100
     for i in range(1, 100+1):
          # Nếu i chia hết cho 3 (dư 0) thì in i ra cách nhau bằng khoảng trắng
          if i%3==0: print(i, end=" ")