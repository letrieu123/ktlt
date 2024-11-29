print("sinh vien:Le Thanh Khanh Trieu MSV:235752021610117")
import math

def giai_phuong_trinh_bac_hai():
    print("Giải phương trình bậc hai: ax² + bx + c = 0")
    
    try:
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        c = float(input("Nhập hệ số c: "))
    except ValueError:
        print("Vui lòng nhập số hợp lệ cho các hệ số.")
        return

    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình có vô số nghiệm.")
            else:
                print("Phương trình vô nghiệm.")
        else:
            x = -c / b
            print(f"Phương trình có nghiệm duy nhất: x = {x}")
    else:
        delta = b**2 - 4*a*c
        print(f"Delta = {delta}")

        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print("Phương trình có hai nghiệm phân biệt:")
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
        elif delta == 0:
            x = -b / (2*a)
            print(f"Phương trình có nghiệm kép: x = {x}")
        else:
            print("Phương trình vô nghiệm thực.")

if __name__ == "__main__":
    giai_phuong_trinh_bac_hai()
