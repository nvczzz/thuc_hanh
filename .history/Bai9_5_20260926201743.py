'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 3 cạnh rồi kiểm tra phải tam giác vuông cân không ?
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
     # map(float, ...) chuyển từng phần tử sang kiểu số thực
     # Nhập dữ liệu, tách theo khoảng trắng và chuyển thành 3 số thực
     a, b, c=map(float, input("Nhập 3 cạnh: ").split())
     # Kiểm tra điều kiện 3 cạnh tạo thành một tam giác
     if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
          # Dùng abs(... ) < 1e-6 để tránh sai số khi dùng số thực
          # Kiểm tra vuông (với độ lệch nhỏ hơn 1e-6) VÀ có 2 cạnh góc vuông bằng nhau
          if ((abs(a**2 + b**2 - c**2) < 1e-6 and a==b) or 
               (abs(a**2 + c**2 - b**2) < 1e-6 and a==c) or 
               (abs(b**2 + c**2 - a**2) < 1e-6 and b==c)):
               # In thông báo nếu là tam giác vuông cân
               print("=> a, b, c là 3 cạnh của 1 tam giác vuông cân !")
          else:
               # In thông báo nếu không thỏa mãn vuông cân
               print("=> a, b, c không phải là 3 cạnh của 1 tam giác vuông cân !")
     else:
          # In thông báo nếu 3 cạnh không tạo thành tam giác
          print("=> a, b, c không phải là 3 cạnh của 1 tam giác !")