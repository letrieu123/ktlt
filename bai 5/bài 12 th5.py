print("sinh vien:le thanh khanh trieu MSV:235752021610117")
import numpy as np

# Dữ liệu đầu vào
student_id = [1023, 5202, 6230, 1671, 1682, 5241, 4532]
student_height = [40., 42., 45., 41., 38., 40., 42.]

# Chuyển danh sách thành mảng NumPy
student_id = np.array(student_id)
student_height = np.array(student_height)

# Sử dụng lexsort() để sắp xếp theo chiều cao trước, sau đó theo id
indices = np.lexsort((student_id, student_height))

# Dữ liệu đã được sắp xếp
sorted_student_id = student_id[indices]
sorted_student_height = student_height[indices]

# In kết quả
print("Thứ tự sắp xếp:", indices)
print("Dữ liệu đã được sắp xếp:")
for id_, height in zip(sorted_student_id, sorted_student_height):
    print(f"ID: {id_}, Chiều cao: {height}")
