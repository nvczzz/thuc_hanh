'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 số rồi kiểm tra có phải là số đặc biệt không ? (Số Armstrong 3 chữ số)
'''

# Định nghĩa hàm kiểm tra số đặc biệt (Tổng lập phương các chữ số bằng chính nó)
def so_dac_biet(n):
    tmp = n   # Tạo biến tạm 'tmp' để lưu giá trị ban đầu của n
    sum = 0   # Biến tích lũy 'sum' dùng để tính tổng lập phương các chữ số
    
    # Kiểm tra nếu n là số có 3 chữ số (nằm trong khoảng từ 1 đến 999)
    if n > 0 and n < 1000:
        # Vòng lặp tách từng chữ số của n từ phải qua trái
        while tmp > 0:
            sum += (tmp % 10) ** 3  # (tmp % 10): lấy chữ số hàng đơn vị; ** 3: tính lập phương rồi cộng vào sum
            tmp //= 10              # tmp //= 10: loại bỏ chữ số hàng đơn vị vừa tính
        # So sánh tổng tính được với giá trị ban đầu n
        return sum == n
    
    # Trả về 0 (False) nếu n không nằm trong khoảng (0, 1000)
    return 0

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
    # Nhập số nguyên từ bàn phím
    n = int(input("Nhập 1 số bất kỳ: "))
    
    # Gọi hàm so_dac_biet(n) và sử dụng toán tử 3 ngôi để in ra kết quả tương ứng
    print("=> Đây là số đặc biệt !" if so_dac_biet(n) else "=> Đây không phải là số đặc biệt !")