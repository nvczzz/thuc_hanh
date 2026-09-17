'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập vào lương và giờ làm việc của 1 nhân viên để tính tiền thưởng
'''

if __name__ == "__main__":
	# map(int, ...) chuyển từng phần tử sang kiểu số ngyên
	luong, gio=map(int, input("Nhập lương và số giờ làm: ").split())
	if gio >= 200:
		print(luong * 0.2)
	elif gio >= 100:
		print(luong * 0.1)
	else:
		print(0)