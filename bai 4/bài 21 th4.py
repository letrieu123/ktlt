print("sinh vien:le thanh khanh trieu MSV:235752021610117")
input_str = input("Nhập chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ")
bin_numbers = input_str.split(',')
divisible_by_5 = []
for bin_num in bin_numbers:
    # Chuyển đổi số nhị phân thành số thập phân
    decimal_value = int(bin_num, 2)
    
    # Kiểm tra nếu số thập phân chia hết cho 5
    if decimal_value % 5 == 0:
        divisible_by_5.append(bin_num)
print(",".join(divisible_by_5))
