print("sinh vien:le thanh khanh trieu MSV:235752021610117")
def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            num_lines = len(lines)
        print(f"Số dòng trong tệp: {num_lines}")
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra đường dẫn.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
file_path = 'th7.txt'
count_lines(file_path)
