'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 3 cạnh rồi kiểm tra phải tam giác cân không ?
'''

if __name__ == "__main__":
     a, b, c=map(int, input("Nhập 3 cạnh: ").split())
     if a>0 and b>0 and c>0 and a+b>c and a+c>b and b+c>a:
          if a==b or b or c and a c:
               print("=> a, b, c là 3 cạnh của 1 tam giác cân !")
          else:
               print("=> a, b, c không phải là 3 cạnh của 1 tam giác cân !")
     else:
          print("=> a, b, c không phải là 3 cạnh của 1 tam giác !")