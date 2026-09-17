'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 4 số rồi in kết quả max và min
'''

if __name__ == "__main__":
	# map(int, ...) chuyển từng phần tử sang kiểu số ngyên
	a, b, c, d=map(int, input("Nhập 4 số: ").split())
	print(f"=> Max =", max(a, b, c, d), "\n=> Min =", min(a, b, c, d))