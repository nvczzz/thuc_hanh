'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 số rồi kiểm tra chẵn/lẻ
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
    # Nhập vào một chuỗi từ bàn phím và ép kiểu dữ liệu sang số nguyên (int)
    num = int(input("Nhập 1 số bất kỳ: "))
    
    # Kiểm tra phép chia lấy phần dư (num % 2 == 0)
    # Dùng toán tử 3 ngôi để in ra kết quả chẵn hoặc lẻ dựa trên điều kiện chia hết cho 2
    print("=> Đây là số chẵn !" if num % 2 == 0 else "=> Đây là số lẻ")