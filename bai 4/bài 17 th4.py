print("sinh vien:le thanh khanh trieu MSV:235752021610117")
n = int(input("Nhập số n: "))
def tong_uoc_so(x):
    tong = 0
    for i in range(1, x):
        if x % i == 0:  # Nếu i là ước số của x
            tong += i
    return tong
print("Các số có tổng các ước số lớn hơn chính nó:")
for i in range(1, n):
    if tong_uoc_so(i) > i:
        print(i)
