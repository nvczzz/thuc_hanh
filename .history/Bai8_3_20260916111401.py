'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu:
'''
import math

if __name__ == "__main__":
     a, b, c=map(float, input("Nhập 3 số: ").split())
     if a==0: print("=> Đây không phải là phương trình trùng phương !")
     else:
          delta=b**2 - 4*a*c
          t1=(-b+math.sqrt(delta))/(2*a)
          t2=(-b-math.sqrt(delta))/(2*a)
          if t1>=0 and t2>=:
               print("=> Phương trình có 4 nghiệm pb là: ")
               print(f"x1 = {math.sqrt(t1:g)}, x2 = -{math.sqrt(t1:g)}")
          

