'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Giải hệ phương trình bậc nhất 2 ẩn (Dùng phương pháp Cramer)
a1*x + b1*y = a3
a2*x + b2*y = b3
'''

if __name__ == "__main__":
    # map(float, ...) chuyển 6 hệ số sang kiểu số thực
    a1, a2, a3, b1, b2, b3 = map(float, input("Nhập 6 số: ").split())
    
    # Tính các định thức Cramer:
    d  = a1 * b2 - b1 * a2   # Định thức chính D
    dx = a3 * b2 - b3 * a2   # Định thức Dx
    dy = a1 * b3 - b1 * a3   # Định thức Dy
    
    # Biện luận nghiệm hệ phương trình dựa theo D, Dx, Dy
    if d == 0:
        if dx == 0 and dy == 0:
            # D = 0 và Dx = Dy = 0 => Vô số nghiệm
            print("=> Hệ phương trình vô số nghiệm !")
        else:
            # D = 0 và (Dx != 0 hoặc Dy != 0) => Vô nghiệm
            print("=> Hệ phương trình vô nghiệm !")
    else:
        # D != 0 => Hệ có nghiệm duy nhất x = Dx / D, y = Dy / D
        print("=> Hệ phương trình có nghiệm là: ")
        print(f"x = {dx/d}")
        print(f"y = {dy/d}")