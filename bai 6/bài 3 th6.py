print("sinh vien:le thanh khanh trieu MSV:235752021610117")
class Nguoi:
    def getGender(self):
        """
        Phương thức chung cho lớp cha, có thể bị ghi đè trong các lớp con.
        """
        return "Không xác định"
class Nam(Nguoi):
    def getGender(self):
        """
        Phương thức cho class Nam, ghi đè phương thức từ lớp cha.
        """
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        """
        Phương thức cho class Nu, ghi đè phương thức từ lớp cha.
        """
        return "Nữ"
# Sử dụng các class
if __name__ == "__main__":
    person1 = Nam()
    person2 = Nu()

    print(f"Giới tính của person1: {person1.getGender()}")
    print(f"Giới tính của person2: {person2.getGender()}")
