'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 4 số rồi in kết quả max và min
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
    # Nhập chuỗi 4 số cách nhau bởi khoảng trắng, tách chuỗi và chuyển từng số về kiểu số nguyên
    # Gán lần lượt vào 4 biến a, b, c, d
    a, b, c, d = map(int, input("Nhập 4 số: ").split())
    
    # Sử dụng F-string để định dạng chuỗi xuất kết quả:
    # max(a, b, c, d): Hàm tìm giá trị lớn nhất trong 4 số
    # min(a, b, c, d): Hàm tìm giá trị nhỏ nhất trong 4 số
    # \n: Ký tự xuống dòng
    print(f"=> Max = {max(a, b, c, d)} \n=> Min = {min(a, b, c, d)}")