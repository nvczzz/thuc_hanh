'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Giải phương trình bậc 2: ax^2 + bx + c = 0
'''
# Khai báo thư viện toán học để sử dụng hàm tính căn bậc hai (math.sqrt)
import math

if __name__ == "__main__":
    # map(float, ...) chuyển các hệ số a, b, c sang kiểu số thực
    a, b, c = map(float, input("Nhập 3 số: ").split())
    
    # Trường hợp a = 0: Phương trình trở thành phương trình bậc nhất bx + c = 0
    if a == 0:
        if b == 0:
            if c == 0:
                print("=> Phương trình vô số nghiệm !")
            else: 
                print("=> Phương trình vô nghiệm !")
        else:
            print(f"=> Phương trình có 1 nghiệm là: x = {-c/b}")
    else:
        # Trường hợp a != 0: Tính Delta (b^2 - 4ac)
        delta = b**2 - 4*a*c
        
        if delta < 0:
            # Delta < 0: Phương trình không có nghiệm thực
            print("=> Phương trình vô nghiệm !")
        elif delta == 0:
            # Delta = 0: Phương trình có nghiệm kép x1 = x2 = -b / (2a)
            print(f"=> Phương trình có nghiệm kép là: x1 = x2 = {-b/(2*a)}")
        else:
            # Delta > 0: Phương trình có 2 nghiệm phân biệt
            print(f"=> Phương trình có 2 nghiệm phân biệt là: x1 = {(-b+math.sqrt(delta))/(2*a)}, x2 = {(-b-math.sqrt(delta))/(2*a)}")