'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu:
'''
import math

if __name__ == "__main__":
     a, b, c=map(float, input("Nhập 3 số: ").split())
     if a==0: 
          print("=> Đây không phải là phương trình trùng phương !")
     else:
          delta=b**2 - 4*a*c
          if delta < 0:
               print("=> Phương trình vô nghiệm !")
          elif delta == 0:
               t=-b/(2*a)
               if t<0:
                    print("=> Phương trình vô nghiệm !")
               elif t==0:
                    print("=> Phương trình có 1 nghiệm là: x=0")
               else:
                    print("=> Phương trình có 2 nghiệm là: ")
                    print(f"x1={math.sqrt(t):g}") 
                    print(f"x2={-math.sqrt(t):g}")
          else:
               t1=(-b+math.sqrt(delta))/(2*a)
               t2=(-b-math.sqrt(delta))/(2*a)
               if t1<0:
                    if t2<0:
                         print("=> Phương trình vô nghiệm !")
                    elif t


