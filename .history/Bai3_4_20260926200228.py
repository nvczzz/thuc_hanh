'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 số rồi kiểm tra có phải là số lẻ âm không ?
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
    # Nhập số từ bàn phím và ép kiểu sang số nguyên
    n = int(input("Nhập 1 số bất kỳ: "))
    
    # Kiểm tra 2 điều kiện kết hợp với toán tử 'and':
    # 1. n % 2 != 0 (n chia 2 có dư, tức là số lẻ)
    # 2. n < 0 (n là số âm)
    # Dùng toán tử 3 ngôi để xuất ra kết quả tương ứng
    print("=> Đây là số lẻ âm !" if n % 2 != 0 and n < 0 else "=> Đây không phải là số lẻ âm")