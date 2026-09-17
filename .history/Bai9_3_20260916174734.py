'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 3 cạnh rồi kiểm tra phải tam giác đều không ?
'''

if __name__ == "__main__":
     # map(float, ...) chuyển từng phần tử sang kiểu số thực
     a, b, c=map(float, input("Nhập 3 cạnh: ").split())
     if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
          # các cacnhj
          if a==b and b == c and a == c:
               print("=> a, b, c là 3 cạnh của 1 tam giác đều !")
          else:
               print("=> a, b, c không phải là 3 cạnh của 1 tam giác đều !")
     else:
          print("=> a, b, c không phải là 3 cạnh của 1 tam giác !")