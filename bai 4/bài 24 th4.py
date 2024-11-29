print("sinh vien:le thanh khanh trieu MSV:235752021610117")
input_str = input("Nhập câu: ")
uppercase_count = 0
lowercase_count = 0
for char in input_str:
    if char.isupper():  # Nếu ký tự là chữ hoa
        uppercase_count += 1
    elif char.islower():  # Nếu ký tự là chữ thường
        lowercase_count += 1
print("Chữ hoa:", uppercase_count)
print("Chữ thường:", lowercase_count)
