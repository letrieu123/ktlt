print("sinh vien:le thanh khanh trieu MSV:235752021610117")
from datetime import datetime, timedelta
# Lấy thời gian hiện tại
current_time = datetime.now()
print("Thời gian hiện tại:", current_time)
# Chuyển đổi thời gian thành chuỗi
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Thời gian được định dạng:", formatted_time)
# Tạo một đối tượng datetime từ chuỗi
date_string = "2024-11-22 14:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Chuỗi được chuyển thành datetime:", parsed_date)
# Tính toán thời gian trong tương lai
future_time = current_time + timedelta(days=5, hours=3)
print("Thời gian sau 5 ngày và 3 giờ:", future_time)
# Tính toán chênh lệch thời gian
time_difference = future_time - current_time
print("Khoảng cách thời gian:", time_difference)
print("Tổng số giây:", time_difference.total_seconds())
