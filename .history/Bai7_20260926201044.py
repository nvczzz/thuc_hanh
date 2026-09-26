'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 tháng rồi kiểm tra xem tháng đó có bao nhiêu ngày
'''

# Kiểm tra xem file có đang được chạy trực tiếp hay không
if __name__ == "__main__":
    # Nhập tháng và ép kiểu sang số nguyên
    th = int(input("Nhập tháng: "))
    
    # Các tháng 1, 3, 5, 7, 8, 10, 12 luôn có 31 ngày
    if th in [1, 3, 5, 7, 8, 10, 12]: 
        print(f"=> Tháng {th} có 31 ngày !")
    elif th == 2:
        # Nếu là tháng 2, cần nhập thêm năm để kiểm tra năm nhuận
        year = int(input("Nhập năm: "))
        
        # Điều kiện năm nhuận: Chia hết cho 400 HOẶC (chia hết cho 4 và không chia hết cho 100)
        # Sử dụng toán tử 3 ngôi để in ra số ngày của tháng 2 (29 ngày nếu nhuận, 28 ngày nếu không)
        print("=> Tháng 2 có 29 ngày !" if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) else "=> Tháng 2 có 28 ngày !")
    else:
        # Các tháng còn lại (4, 6, 9, 11) có 30 ngày
        print(f"=> Tháng {th} có 30 ngày !")