print("sinh vien: Le Thanh Khanh Trieu MSV:235752021610117")
def square(n):
    """Trả về bình phương của n."""
    return n * n
def cube(n):
    """Trả về lập phương của n."""
    return n * n * n
def average(values):
    """Trả về giá trị trung bình của danh sách các giá trị."""
    nvals = len(values)
    sum = 0.0
    for v in values:
        sum += v
    return float(sum) / nvals if nvals > 0 else 0  
