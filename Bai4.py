'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 2 số rồi hoán đổi vị trí
'''

if __name__ == "__main__":
	# map(int, ...) chuyển từng phần tử sang kiểu số ngyên
	num1, num2 = map(int, input("Nhập 2 số: ").split())
	# hoán đổi 2 số
	num1, num2 = num2, num1
	print(num1, num2)