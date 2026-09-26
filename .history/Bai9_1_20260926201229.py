'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 3 cạnh rồi kiểm tra phải tam giác không ?
'''

if __name__ == "__main__":
    # map(float, ...) chuyển 3 độ dài nhập vào sang kiểu số thực
    a, b, c = map(float, input("Nhập 3 cạnh: ").split())
    
    # Điều kiện để a, b, c là 3 cạnh của 1 tam giác:
    # 1. Các cạnh đều phải lớn hơn 0 (a > 0, b > 0, c > 0)
    # 2. Bất đẳng thức tam giác: Tổng 2 cạnh bất kỳ luôn lớn hơn cạnh còn lại
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        print("=> a, b, c là 3 cạnh của 1 tam giác !")
    else:
        print("=> a, b, c không phải là 3 cạnh của 1 tam giác")