'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Giải hệ phương trình bậc nhất 2 ẩn
'''

if __name__ == "__main__":
     a1, a2, a3, b1, b2, b3=map(float, input("Nhập 6 số: ").split())
     d= a1*b2 - a2*b1
     dx= a2*b3 - b2*a3
     dy= a1*b3 - b1*a3
     if d==0:
          if dx==0 and dy==0:
               print("=> Hệ phương trình vô số nghiệm !")
          else:
               print("=> Hệ phương trình vô nghiệm !")
     else:
          print("=> Hệ phương trình có nghiệm duy nhất là: ")
          print(f"x = {dx/d}")
          print(f"y = {d}")