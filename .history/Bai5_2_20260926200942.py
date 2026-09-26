'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 4 số rồi sắp xếp tăng và giảm dần
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
    # map(int, ...) chuyển từng phần tử nhập vào sang kiểu số nguyên
    a, b, c, d = map(int, input("Nhập 4 số: ").split())
    
    # sorted([a, b, c, d]): Tạo một danh sách được sắp xếp tăng dần từ 4 số
    # Toán tử * (Unpacking): Giải nén danh sách để in các phần tử cách nhau bởi khoảng trắng
    # reverse=1 (hoặc reverse=True): Sắp xếp danh sách theo thứ tự giảm dần
    print("=> Thứ tự tăng dần:", *sorted([a, b, c, d]), "\n=> Thứ tự giảm dần:", *sorted([a, b, c, d], reverse=1))