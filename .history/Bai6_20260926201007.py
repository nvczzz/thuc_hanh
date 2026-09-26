'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập 1 kí tự rồi kiểm tra là nguyên âm, phụ âm, ký tự số, ký tự khác
'''


if __name__ == "__main__":
    # Nhập một ký tự bất kỳ từ bàn phím
    ch = input("Nhập 1 kí tự: ")
    
    # ch.lower(): Chuyển ký tự thành chữ thường để so sánh không phân biệt hoa/thường
    if ch.lower() in "ueoai": 
        # Kiểm tra nếu ký tự nằm trong chuỗi các nguyên âm
        print("=> Đây là nguyên âm !")
    elif ch.isalpha(): 
        # ch.isalpha(): Kiểm tra xem ký tự có phải là chữ cái (Alphabet) không
        print("=> Đây là phụ âm !")
    elif ch.isdigit(): 
        # ch.isdigit(): Kiểm tra xem ký tự có phải là chữ số (0-9) không
        print("=> Đây là ký tự số !")
    else: 
        # Trường hợp ký tự đặc biệt, dấu câu, khoảng trắng...
        print("=> Đây là ký tự khác !")