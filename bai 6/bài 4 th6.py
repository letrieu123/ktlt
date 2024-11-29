print("sinh vien:le thanh khanh trieu MSV:235752021610117")
class RomanToInteger:
    def __init__(self):
        """
        Khởi tạo với bảng ánh xạ các ký tự La Mã và giá trị tương ứng.
        """
        self.roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    def convert(self, roman):
        """
        Chuyển đổi một số La Mã thành số nguyên.
        :param roman: Chuỗi La Mã cần chuyển đổi (str).
        :return: Số nguyên tương ứng (int).
        """
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = self.roman_to_int_map.get(char, 0)
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total
# Sử dụng class
if __name__ == "__main__":
    converter = RomanToInteger()
    roman_number = "MCMXCIV" 
    integer_value = converter.convert(roman_number)
    print(f"Số La Mã '{roman_number}' chuyển đổi thành số nguyên là: {integer_value}")
