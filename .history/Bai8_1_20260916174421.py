'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Giải phương trình bậc nhất: ax+b=0
'''

if __name__ == "__main__":
     # map(int, ...) chuyển từng phần tử sang kiểu số ngyên
     a, b=map(float, input("Nhập 2 số: ").split())
     if a==0:
          if b==0:
               print("=> Phương trình vô số nghiệm !")
          else:
               print("=> Phương trình vô nghiệm !")
     else:
          print(f"=> Phương trình có 1 nghiệm là: x = {-b/a}")