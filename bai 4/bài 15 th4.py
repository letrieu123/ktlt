print ("sinh vien:Le Thanh Khanh Trieu MSV:235752021610117")
chuoi = input("Nhập các từ tiếng Anh cách nhau bởi dấu cách: ")
danh_sach_tu = chuoi.split()
danh_sach_tu.sort()
print("Các từ theo thứ tự từ điển:")
for tu in danh_sach_tu:
    print(tu)
