print ("sinh vien:Le Thanh Khanh Trieu MSV:235752021610117")
#Yêu cầu tách họ và tên
name = input("Nhập họ và tên: ").strip()

#Tách chuỗi dựa vào dấu cách
parts = name.split()

#Kiểm tra nếu chuỗi gồm ít nhất hai phần
if len(parts) >= 2:
    last_name = parts[0] #Phần họ
    first_name = parts[-1] #Phần tên riêng
    print("Họ:", last_name)
    print("Tên riêng:", first_name)
else:
    print("Nhập đầy đủ họ tên")
