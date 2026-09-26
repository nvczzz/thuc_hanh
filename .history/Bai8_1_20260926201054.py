'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Giải phương trình bậc nhất: ax + b = 0
'''

if __name__ == "__main__":
    # map(float, ...) chuyển các hệ số nhập vào sang kiểu số thực
    a, b = map(float, input("Nhập 2 số: ").split())
    
    # Kiểm tra trường hợp hệ số a = 0
    if a == 0:
        if b == 0:
            # Dạng 0x + 0 = 0 (Thỏa mãn với mọi x)
            print("=> Phương trình vô số nghiệm !")
        else:
            # Dạng 0x + b = 0 với b != 0 (Mâu thuẫn)
            print("=> Phương trình vô nghiệm !")
    else:
        # Dạng ax + b = 0 với a != 0 => x = -b / a
        print(f"=> Phương trình có 1 nghiệm là: x = {-b/a}")