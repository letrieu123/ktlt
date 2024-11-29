print("sinh vien:le thanh khanh trieu MSV:235752021610117")
class ReverseWords:
    def __init__(self, input_string):
        """
        Khởi tạo với chuỗi đầu vào.
        :param input_string: Chuỗi cần xử lý (str).
        """
        self.input_string = input_string
    def reverse_words(self):
        """
        Đảo ngược thứ tự các từ trong chuỗi.
        :return: Chuỗi đã đảo ngược thứ tự từ (str).
        """
        # Tách các từ bằng khoảng trắng, đảo ngược danh sách từ, và ghép lại thành chuỗi
        reversed_string = ' '.join(self.input_string.split()[::-1])
        return reversed_string
# Sử dụng class
if __name__ == "__main__":
    input_text = "hello .py"
    reverser = ReverseWords(input_text)
    result = reverser.reverse_words()
    print(f"Chuỗi đầu vào: '{input_text}'")
    print(f"Chuỗi sau khi đảo ngược: '{result}'")
