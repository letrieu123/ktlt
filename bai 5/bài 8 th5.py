print("sinh vien:le thanh khanh trieu MSV:235752021610117")
# Module tìm kiếm tuyến tính
def Sequential_Search(dlist, item):
    for index, value in enumerate(dlist):
        if value == item:
            return True, index  # Trả về True và vị trí tìm thấy
    return False, -1  # Trả về False nếu không tìm thấy

# Hàm chính
def main():
    # Nhập số lượng phần tử trong danh sách
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    
    # Nhập các phần tử của danh sách
    dlist = []
    for i in range(n):
        value = int(input(f"Nhập phần tử thứ {i+1}: "))
        dlist.append(value)
    
    # Nhập phần tử cần tìm
    item = int(input("Nhập phần tử cần tìm: "))
    
    # Gọi hàm Sequential_Search
    found, position = Sequential_Search(dlist, item)
    
    # In ra kết quả
    if found:
        print(f"Phần tử {item} được tìm thấy ở vị trí {position}.")
    else:
        print(f"Phần tử {item} không có trong danh sách.")

# Gọi hàm chính
if __name__ == "__main__":
    main()
