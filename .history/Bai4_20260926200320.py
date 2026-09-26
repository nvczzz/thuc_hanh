'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 2 số rồi hoán đổi vị trí
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
    # Nhập chuỗi từ bàn phím, tách thành các phần tử riêng biệt bằng split()
    # map(int, ...) ép kiểu từng phần tử sang kiểu số nguyên
    # Gán giá trị vào 2 biến num1 và num2
    num1, num2 = map(int, input("Nhập 2 số: ").split())
    
    # Thực hiện hoán đổi giá trị của 2 biến bằng cơ chế Tuple Unpacking trong Python
    num1, num2 = num2, num1
    
    # In ra giá trị của num1 và num2 sau khi đã hoán đổi
    print(num1, num2)