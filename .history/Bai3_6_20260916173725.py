'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 số rồi kiểm tra có phải là số đặc biệt không ?
'''
# hàm kiểm tra số đăc
def so_dac_biet(n):
	tmp=n
	sum=0
	if n>0 and n<1000:
		while tmp>0:
			sum+=(tmp%10)**3
			tmp//=10
		return sum == n
	return 0

if __name__ == "__main__":
	n=int(input("Nhập 1 số bất kỳ: "))
	# Dùng toán tử 3 ngôi 
	print("=> Đây là số đặc biệt !" if so_dac_biet(n) else "=>Đây không phải là số đặc biệt !")