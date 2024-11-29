print("sinh vien:le thanh khanh trieu MSV:235752021610117")
n = int(input("Nhập số nguyên n: "))
def fibonacci(n):
    fib_list = []  # Danh sách để chứa các số Fibonacci
    a, b = 0, 1  # Các giá trị ban đầu của dãy Fibonacci
    while a < n:
        fib_list.append(a)
        a, b = b, a + b  # Cập nhật các giá trị Fibonacci tiếp theo
    return fib_list
fib_list = fibonacci(n)
print("Danh sách các số Fibonacci nhỏ hơn", n, "là:", fib_list)
