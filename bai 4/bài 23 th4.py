print("sinh vien:le thanh khanh trieu MSV:235752021610117")
input_str = input("Nhập câu: ")
letter_count = 0
digit_count = 0
for char in input_str:
    if char.isalpha():  # Nếu ký tự là chữ cái
        letter_count += 1
    elif char.isdigit():  # Nếu ký tự là chữ số
        digit_count += 1
print("Số chữ cái là:", letter_count)
print("Số chữ số là:", digit_count)
