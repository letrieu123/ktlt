print("sinh vien:le thanh khanh trieu MSV:235752021610117")
def sap_xep_danh_sach(danh_sach):
    return sorted(danh_sach)
def tim_phan_tu_lon_nhat(danh_sach):
    return max(danh_sach)
def main():
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    danh_sach = []
    for i in range(n):
        gia_tri = float(input(f"Nhập phần tử thứ {i+1}: "))
        danh_sach.append(gia_tri)
    danh_sach_sap_xep = sap_xep_danh_sach(danh_sach)
    print("Danh sách sau khi sắp xếp:", danh_sach_sap_xep)
    max_value = tim_phan_tu_lon_nhat(danh_sach)
    min_value = danh_sach_sap_xep[0]  
    print("Phần tử lớn nhất:", max_value)
    print("Phần tử nhỏ nhất:", min_value)
if __name__ == "__main__":
    main()
