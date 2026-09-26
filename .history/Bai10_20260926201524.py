'''
Name: Nguyễn Văn Chung
Date: 15/9/2026
Mô tả yêu cầu: Nhập điểm rồi xét học bổng
'''  # Ghi chú tiêu đề và thông tin bài tập[cite: 3].

if __name__ == "__main__":  # Điểm bắt đầu chạy chương trình[cite: 3].
    diem = float(
        input("Nhập điểm: ")
    )  # Nhập điểm từ bàn phím và ép kiểu về số thực float[cite: 3].
    if diem >= 9:  # Nếu điểm lớn hơn hoặc bằng 9[cite: 3]
        print(5000000)  # In mức học bổng là 5.000.000[cite: 3]
    elif diem >= 8:  # Nếu điểm nằm trong khoảng [8, 9)[cite: 3]
        print(3000000)  # In mức học bổng là 3.000.000[cite: 3]
    elif diem >= 7:  # Nếu điểm nằm trong khoảng [7, 8)[cite: 3]
        print(1000000)  # In mức học bổng là 1.000.000[cite: 3]
    else:  # Trường hợp điểm dưới 7[cite: 3]
        print(0)  # In mức học bổng là 0[cite: 3]