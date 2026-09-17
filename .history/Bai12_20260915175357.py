'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập tuổi rồi kết luận lứa t
'''

if __name__ == "__main__":
     age=int(input("Nhập tuổi: "))
     if age > 50:
          print("Cao niên")
     elif age > 39:
          print("Trung niên")
     elif age > 17:
          print("Thanh niên") 
     elif age > 10:
          print("Vị thành niên")
     elif age > 2:
          print("Nhi đồng")
     else:
          print("Trẻ sơ sinh")