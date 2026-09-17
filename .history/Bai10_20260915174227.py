'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập điểm rồi tính học 
'''

if __name__ == "__main__":
     diem=float(input("Nhập điểm: "))
     if diem >= 9:
          print(5000000)
     elif diem >= 8:
          print(3000000)
     elif diem >= 7:
          print(1000000)
     else:
          print(0)