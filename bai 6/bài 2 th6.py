print("sinh vien:le thanh khanh trieu MSV:235752021610117")
class Hinhchunhat:
    def __init__(self, chieudai, chieurong):
        """
        Hàm khởi tạo class Hinhchunhat.
        :param chieudai: Chiều dài của hình chữ nhật (float hoặc int).
        :param chieurong: Chiều rộng của hình chữ nhật (float hoặc int).
        """
        self.chieudai = chieudai
        self.chieurong = chieurong
    def dientich(self):
        """
        Tính diện tích hình chữ nhật.
        :return: Diện tích của hình chữ nhật (float hoặc int).
        """
        return self.chieudai * self.chieurong
# Sử dụng class Hinhchunhat
if __name__ == "__main__":
    # Tạo đối tượng Hinhchunhat
    hcn = Hinhchunhat(10, 5)  # Chiều dài 10, chiều rộng 5
    # Tính diện tích
    print
    (f"Diện tích hình chữ nhật có chiều dài {hcn.chieudai} và chiều rộng {hcn.chieurong} là: {hcn.dientich()}")
