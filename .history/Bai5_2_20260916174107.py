'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 4 số rồi sắp xếp tăng và giảm dần
'''

if __name__ == "__main__":
	
	a, b, c, d = map(int, input("Nhập 4 số: ").split())
	print("=> Thứ tự tăng dần:", *sorted([a, b, c, d]), "\n=> Thứ tự giảm dần:", *sorted([a, b, c, d], reverse=1))