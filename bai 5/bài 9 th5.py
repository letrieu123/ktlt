print ("sinh vien:le thanh khanh trieu MSV:235752021610117")
def binary_search(lst, value):
    lowerBound = 0
    upperBound = len(lst) - 1
    
    while lowerBound <= upperBound:
        midPoint = lowerBound + (upperBound - lowerBound) // 2
        if lst[midPoint] == value:
            return True  # Tìm thấy phần tử
        elif lst[midPoint] < value:
            lowerBound = midPoint + 1
        else:
            upperBound = midPoint - 1
    
    return False  # Không tìm thấy phần tử
lst = list(map(int, input("Nhập danh sách đã sắp xếp, ngăn cách bằng dấu cách: ").split()))
value = int(input("Nhập phần tử cần tìm: "))
# Gọi hàm tìm kiếm nhị phân
result = binary_search(lst, value)
print("Kết quả tìm kiếm:", result)
