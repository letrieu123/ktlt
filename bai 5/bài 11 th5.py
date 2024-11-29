print("sinh vien:le thanh khanh trieu MSV:235752021610117")
import numpy as np

# Dữ liệu đầu vào
data = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
]

# Định nghĩa cấu trúc của mảng
dtype = [('name', 'U10'), ('class', 'i4'), ('height', 'f4')]

# Tạo mảng có cấu trúc
students = np.array(data, dtype=dtype)

# Sắp xếp theo lớp trước, sau đó theo chiều cao
sorted_students = np.sort(students, order=['class', 'height'])

# In kết quả
print(sorted_students)
