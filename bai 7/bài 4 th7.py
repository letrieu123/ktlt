print("sinh vien:le thanh khanh trieu MSV:235752021610117")
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print("Nội dung của tệp:")
        print(content)
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra đường dẫn.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_path = 'th7.txt'
read_file(file_path)