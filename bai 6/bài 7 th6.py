print("sinh vien:le thanh khanh trieu MSV:235752021610117")
import math
class Circle:
    def __init__(self, radius):
        """
        Khởi tạo class Circle với bán kính.
        :param radius: Bán kính của hình tròn (float hoặc int).
        """
        self.radius = radius
    def area(self):
        """
        Tính diện tích của hình tròn.
        :return: Diện tích (float).
        """
        return math.pi * (self.radius ** 2)
    def circumference(self):
        """
        Tính chu vi của hình tròn.
        :return: Chu vi (float).
        """
        return 2 * math.pi * self.radius
# Sử dụng class
if __name__ == "__main__":
    # Tạo một đối tượng Circle với bán kính 10
    circle = Circle(10)
    # Tính diện tích và chu vi
    print(f"Diện tích hình tròn có bán kính {circle.radius} là: {circle.area():.2f}")
    print(f"Chu vi hình tròn có bán kính {circle.radius} là: {circle.circumference():.2f}")
