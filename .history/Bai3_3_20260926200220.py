'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 số rồi kiểm tra có phải là số chẵn dương không ?
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
    # Nhập dữ liệu đầu vào và chuyển đổi thành số nguyên
    n = int(input("Nhập 1 số bất kỳ: "))
    
    # Kiểm tra 2 điều kiện đồng thời bằng toán tử 'and':
    # 1. n % 2 == 0 (n là số chẵn)
    # 2. n > 0 (n là số dương)
    # Dùng toán tử 3 ngôi để thực hiện việc in thông báo tương ứng
    print("=> Đây là số chẵn dương !" if n % 2 == 0 and n > 0 else "=> Đây không phải là số chẵn dương !")