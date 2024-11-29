print('sinh vien:le thanh khanh trieu MSV:235752021610117')
import numpy as np
#tạo kiểu cấu trúc cho mảng
dtype = [('name', 'U50'), ('height', 'f4'), ('class', 'U20')]
#dữ liệu của sinh viên
data = [
    ('Alice', 1.65, '10A'),
    ('Bob', 1.80, '10B'),
    ('Charlie', 1.70, '10C'),
    ('David', 1.75, '10A'),
    ('Eva', 1.60, '10B')
]
#tạo mảng numpy có kiểu dữ liệu cấu trúc
students = np.array(data, dtype=dtype)
#sắp xếp mảng theo chiều cao tăng dần
sorted_students = np.sort(students, order='height')
#in ra kết quả
print("danh sách sinh viên đã sắp xếp theo chiều cao:")
for student in sorted_students:
    print(f"tên:{student['name']}, chiều cao:{student['height']}, lớp:{student['class']}")