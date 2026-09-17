'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 số rồi kiểm tra chẵn/lẻ
'''

if __name__ == "__main__":
	num=int(input("Nhập 1 số bất kỳ: "))
	print("=> Đây là số chẵn !" if num % 2 == 0 else "=> Đây là số lẻ")