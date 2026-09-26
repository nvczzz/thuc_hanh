'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Giải phương trình trùng phương: ax^4 + bx^2 + c = 0
'''
import math

if __name__ == "__main__":
    # map(float, ...) chuyển 3 hệ số sang kiểu số thực
    a, b, c = map(float, input("Nhập 3 số: ").split())
    
    # Kiểm tra nếu a = 0 thì không phải phương trình trùng phương bậc 4
    if a == 0: 
        print("=> Đây không phải là phương trình trùng phương !")
    else:
        # Đặt t = x^2 (Điều kiện t >= 0), phương trình trở thành: at^2 + bt + c = 0
        delta = b**2 - 4*a*c
        
        if delta < 0:
            print("=> Phương trình vô nghiệm !")
        elif delta == 0:
            # Nghiệm t duy nhất
            t = -b / (2 * a)
            if t < 0:
                print("=> Phương trình vô nghiệm !")
            elif t == 0:
                print("=> Phương trình có 1 nghiệm là: x = 0")
            else:
                # Với t > 0 => x = ±√t
                # Định dạng :g để in số gọn gàng (bỏ các số 0 thừa đằng sau)
                print("=> Phương trình có 2 nghiệm là: ")
                print(f"x1 = {math.sqrt(t):g}") 
                print(f"x2 = {-math.sqrt(t):g}")
        else:
            # Delta > 0: Tìm được 2 nghiệm t1 và t2
            t1 = (-b + math.sqrt(delta)) / (2 * a)
            t2 = (-b - math.sqrt(delta)) / (2 * a)
            
            # Xét các trường hợp dấu của t1 và t2 để suy ra nghiệm x
            if t1 < 0:
                if t2 < 0:
                    print("=> Phương trình vô nghiệm !")
                elif t2 == 0:
                    print("=> Phương trình có 1 nghiệm: x = 0")
                else:
                    print("=> Phương trình có 2 nghiệm là: ")
                    print(f"x1 = {math.sqrt(t2):g}")
                    print(f"x2 = {-math.sqrt(t2):g}")
            elif t1 == 0:
                if t2 < 0:
                    print("=> Phương trình có 1 nghiệm là: x = 0")
                else:
                    print("=> Phương trình có 3 nghiệm là: ")
                    print(f"x1 = {math.sqrt(t2):g}")
                    print(f"x2 = {-math.sqrt(t2):g}")
                    print("x3 = 0")
            else:
                if t2 < 0:
                    print("=> Phương trình có 2 nghiệm là: ")
                    print(f"x1 = {math.sqrt(t1):g}")
                    print(f"x2 = {-math.sqrt(t1):g}")
                elif t2 == 0:
                    print("=> Phương trình có 3 nghiệm là: ")
                    print(f"x1 = {math.sqrt(t1):g}")
                    print(f"x2 = {-math.sqrt(t1):g}")
                    print("x3 = 0")
                else:
                    print("=> Phương trình có 4 nghiệm là: ")
                    print(f"x1 = {math.sqrt(t1):g}")
                    print(f"x2 = {-math.sqrt(t1):g}")
                    print(f"x3 = {math.sqrt(t2):g}")
                    print(f"x4 = {-math.sqrt(t2):g}")