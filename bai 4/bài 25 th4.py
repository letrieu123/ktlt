print("sinh vien:le thanh khanh trieu MSV:235752021610117")
input_str = input("Nhập dãy số, cách nhau bằng dấu phẩy: ")
num_list = [int(x) for x in input_str.split(',')]  
# Lọc các số lẻ
odd_numbers = [num for num in num_list if num % 2 != 0]
print(",".join(map(str,odd_numbers)))
