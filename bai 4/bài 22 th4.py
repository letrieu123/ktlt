print("sinh vien:le thanh khanh trieu MSV:235752021610117")
def all_even_digits(num):
    for digit in str(num):  # Duyệt qua từng chữ số của số
        if digit not in '02468':  # Nếu chữ số không phải là 0, 2, 4, 6, 8
            return False
    return True
result = []
for num in range(1000, 3001):
    if all_even_digits(num):
        result.append(str(num))  # Lưu số vào danh sách dưới dạng chuỗi
print(",".join(result))
