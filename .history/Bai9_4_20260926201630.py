'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 3 cạnh rồi kiểm tra phải tam giác vuông không ?
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
     # map(float, ...) chuyển từng phần tử sang kiểu số thực
     # Nhập chuỗi các cạnh, tách theo khoảng trắng và chuyển thành kiểu số thực
     a, b, c=map(float, input("Nhập 3 cạnh: ").split())
     # Kiểm tra điều kiện 3 cạnh tạo thành một tam giác hợp lệ
     if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
          # tổng bình phương 2 cạnh = bình phương cạnh còn lại là tam giác vuông
          # Kiểm tra điều kiện định lý Pitago
          if (a**2 + b**2)==c**2 or (a**2 + c**2)==b**2 or (b**2 + c**2)==a**2:
               # In kết quả nếu là tam giác vuông
               print("=> a, b, c là 3 cạnh của 1 tam giác vuông !")
          else:
               # In kết quả nếu không phải tam giác vuông
               print("=> a, b, c không phải là 3 cạnh của 1 tam giác vuông !")
     else:
          # In kết quả nếu không tạo thành tam giác
          print("=> a, b, c không phải là 3 cạnh của 1 tam giác !")