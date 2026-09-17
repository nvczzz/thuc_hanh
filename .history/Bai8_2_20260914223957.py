'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: ax^2 + bx + c = 0
'''

if __name__ == "__main__":
     a, b, c=map(float, input("Nhập 3 số: ".split()))
     if a==0:
          if b==0:
               if c==0:
                    print("=> Phương trình vô số nghiệm !")
               else: 
                    print("=> Phương trình vô nghiệm !")
          else:
               print(f"=> Phương trình có 1 nghiệm là: x = {-b/c}")
     else:
          delta = b**2 - (4*a*c)
          if delta < 0:
               print("=> Phương trình vô nghiệm !")
          elif delt