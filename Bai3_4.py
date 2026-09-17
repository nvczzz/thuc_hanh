'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 số rồi kiểm tra có phải là số lẻ âm không ?
'''

if __name__ == "__main__":
	n=int(input("Nhập 1 số bất kỳ: "))
	# Dùng toán tử 3 ngôi 
	print("=> Đây là số lẻ âm !" if n%2!=0 and n<0 else "=> Đây không phải là số lẻ âm")