'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 3 cạnh rồi kiểm tra phải tam giác đều không ?
'''

if __name__ == "__main__":
    # map(float, ...) chuyển 3 độ dài nhập vào sang kiểu số thực
    a, b, c = map(float, input("Nhập 3 cạnh: ").split())
    
    # Bước 1: Kiểm tra điều kiện để tạo thành một tam giác hợp lệ
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        # Bước 2: Kiểm tra tam giác đều (cả 3 cạnh bằng nhau)
        if a == b and b == c and a == c:
            print("=> a, b, c là 3 cạnh của 1 tam giác đều !")
        else:
            print("=> a, b, c không phải là 3 cạnh của 1 tam giác đều !")
    else:
        print("=> a, b, c không phải là 3 cạnh của 1 tam giác !")