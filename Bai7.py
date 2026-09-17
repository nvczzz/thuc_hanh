'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 tháng rồi kiểm tra xem tháng đó có bao nhiêu ngày
'''

if __name__ == "__main__":
	th=int(input("Nhập tháng: "))
	if th in [1,3,5,7,8,10,12]: print(f"=> Tháng {th} có 31 ngày !")
	elif th == 2:
		year=int(input("Nhập năm: "))
		# Dùng toán tử 3 ngôi 
		print("=> Tháng 2 có 29 ngày !" if year%400==0 or (year%4==0 and year%100!=0) else "=> Tháng 2 có 28 ngày !")
	else:
		print(f"=> Tháng {th} có 30 ngày !")	