'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 số rồi kiểm tra có phải là số chính phương không ?
'''

# Import (khai báo) thư viện math để sử dụng các hàm toán học
import math

# Định nghĩa hàm kiểm tra số chính phương
def so_chinh_phuong(n):
    # Số chính phương phải là số không âm. Nếu n < 0 thì trả về 0 (False)
    if n < 0: 
        return 0
    # math.sqrt(n): Tính căn bậc hai của n (trả về kiểu số thực float)
    # int(math.sqrt(n)): Lấy phần nguyên của căn bậc hai
    # So sánh phần nguyên của căn với giá trị căn thực tế; nếu bằng nhau thì n là số chính phương
    return int(math.sqrt(n)) == math.sqrt(n)	

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
    # Nhập dữ liệu đầu vào từ bàn phím và ép kiểu sang số nguyên
    n = int(input("Nhập 1 số bất kỳ: "))
    
    # Gọi hàm so_chinh_phuong(n) kết hợp với toán tử 3 ngôi để in thông báo kết quả
    print("=> Đây là số chính phương !" if so_chinh_phuong(n) else "=> Đây không phải là số chính phương !")