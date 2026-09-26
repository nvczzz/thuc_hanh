'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập vào lương và giờ làm việc của 1 nhân viên để tính tiền thưởng
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
    # Nhập chuỗi từ bàn phím, tách thành các phần tử bằng split()
    # map(int, ...) chuyển từng phần tử vừa tách sang kiểu số nguyên (int)
    # Gán lần lượt hai giá trị thu được vào 2 biến luong và gio
    luong, gio = map(int, input("Nhập lương và số giờ làm: ").split())
    
    # Kiểm tra điều kiện số giờ làm việc để tính tiền thưởng
    if gio >= 200:
        # Nếu số giờ >= 200: Tiền thưởng = 20% lương
        print(luong * 0.2)
    elif gio >= 100:
        # Nếu 100 <= số giờ < 200: Tiền thưởng = 10% lương
        print(luong * 0.1)
    else:
        # Nếu số giờ < 100: Không có thưởng (0)
        print(0)