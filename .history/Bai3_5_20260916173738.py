'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 số rồi kiểm tra có phải là số chính phương không ?
'''

# khai báo thư viện toán học
import math

# hàm kiểm tra số chính phương không ?
def so_chinh_phuong(n):
	if n<0: return 0
	return int(math.sqrt(n)) == math.sqrt(n)	

if __name__ == "__main__":
	n=int(input("Nhập 1 số bất kỳ: "))
	# Dùng toán tử 3 ngôi 
	print("=> Đây là số chính phương !" if so_chinh_phuong(n) else "=> Đây không phải là số chính phương !")