print("sinh vien:le thanh khanh trieu MSV:235752021610117")
class StringProcessor:
    def __init__(self):
        """
        Khởi tạo class với một thuộc tính để lưu trữ chuỗi.
        """
        self.string = ""
    def get_String(self):
        """
        Nhận một chuỗi từ người dùng và lưu vào thuộc tính.
        """
        self.string = input("Nhập chuỗi: ")
    def print_String(self):
        """
        In chuỗi đã nhập dưới dạng chữ in hoa.
        """
        print("Chuỗi in hoa:", self.string.upper())
# Sử dụng class
if __name__ == "__main__":
    processor = StringProcessor()
    # Gọi phương thức để lấy chuỗi từ người dùng
    processor.get_String()
    # In chuỗi dưới dạng chữ in hoa
    processor.print_String()
