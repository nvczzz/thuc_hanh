'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 số đến khi thoả mãn điều kiện: 0 < n < 100
'''

if __name__ == "__main__":
     # 
     while True:
          n=int(input("Nhập số trong khoảng từ 0 đến 100: "))
          if 0 < n < 100: break
     print("=> Số bạn nhập là:", n)
