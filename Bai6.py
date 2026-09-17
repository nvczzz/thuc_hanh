'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 kí tự rồi kiểm tra là nguyên âm, phụ âm, ký tự số, ký tự khác
'''

if __name__ == "__main__":
	ch=input("Nhập 1 kí tự: ")
	if ch.lower() in "ueoai": print("=> Đây là nguyên âm !")
	elif ch.isalpha(): print("=> Đây là phụ âm !")
	elif ch.isdigit(): print("=> Đây là ký tự số !")
	else: print("=> Đây là ký tự khác !")