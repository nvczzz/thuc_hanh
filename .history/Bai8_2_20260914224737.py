'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: ax^2 + bx + c = 0
'''

impỏt
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
          elif delta == 0:
               print(f"=> Phương trình có nghiệm kép là: x1 = x2 = {-b/2*a}")
          else:
               print(f"=> Phương trình có 2 nghiệm phân biệt là: x1 = {-b+math.sqrtf(delta)/2*a}", ", x2 = {-b-math.sqrtf(delta)/2*a}")