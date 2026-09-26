'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 số bất kỳ rồi kiểm tra có phải là số nguyên không ?
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
    # Nhập dữ liệu đầu vào từ bàn phím (kết quả trả về là một chuỗi ký tự)
    n = input("Nhập 1 số bất kỳ: ")
    
    # n.isdigit() kiểm tra xem chuỗi n có chứa hoàn toàn các chữ số hay không
    # Dùng toán tử 3 ngôi (Ternary Operator): [Giá trị nếu Đúng] if [Điều kiện] else [Giá trị nếu Sai]
    print("=> Đây là số nguyên !" if n.isdigit() else "=> Đây không phải là số nguyên !")