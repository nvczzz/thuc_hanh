'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 số bất kỳ rồi kiểm tra có phải là số nguyên không ?
'''

if __name__ == "__main__":
	n=input("Nhập 1 số bất kỳ: ")
	print("=> Đây là số nguyên !" if n.isdigit() else "=> Đây không phải là số nguyên !")