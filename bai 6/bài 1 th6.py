print("sinh vien:le thanh khanh trieu MSV:235752021610117")
import math
class Circle:
    def __init__(self, radius):
        """
        Hàm khởi tạo class Circle.
        :param radius: Bán kính của hình tròn (float hoặc int).
        """
        self.radius = radius
    def area(self):
        """
        Tính diện tích hình tròn.
        :return: Diện tích hình tròn (float).
        """
        return math.pi * (self.radius ** 2)
# Sử dụng class Circle
if __name__ == "__main__":
    # Tạo một đối tượng Circle
    circle = Circle(5)  # Bán kính là 5

    # Tính diện tích
    print(f"Diện tích hình tròn có bán kính {circle.radius} là: {circle.area():.2f}")
