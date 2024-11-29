print("sinh vien:le thanh khanh trieu MSV:235752021610117")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
def pascal_value(k, r):
    return factorial(k) // (factorial(r) * factorial(k - r))
def print_pascals_triangle(n):
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(pascal_value(i, j))
        print(" ".join(map(str, row)))
n = int(input("Nhập số dòng cần in của tam giác Pascal: "))
print_pascals_triangle(n)
