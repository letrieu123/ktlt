print ("sih vien:Le Thanh Khanh Trieu MSV:235752021610117")
# Nhập chuỗi từ bàn phím
chuoi = input("Nhập một chuỗi: ")

# Loại bỏ các chữ số khỏi chuỗi
chuoi_moi = ''.join(c for c in chuoi if not c.isdigit())

# In ra chuỗi mới
print("Chuỗi sau khi loại bỏ các chữ số:", chuoi_moi)
