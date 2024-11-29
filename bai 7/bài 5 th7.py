print("sinh vien:le thanh khanh trieu MSV:235752021610117")
# Mở tệp ở chế độ 'append' để nối văn bản vào tệp
file_path = 'th7.txt'
# Văn bản cần nối vào tệp
text_to_append = "Đây là văn bản mới được nối vào tệp.\n"
# Mở tệp và nối văn bản
with open(file_path, 'a', encoding='utf-8') as file:
    file.write(text_to_append)
# Mở tệp ở chế độ đọc để hiển thị nội dung
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
# Hiển thị nội dung của tệp
print(content)