print("sinh vien:le thanh khanh trieu MSV:235752021610117")
balance = 1000000 # Số dư ban đầu 
def display_menu():  # Hàm hiển thị menu
    print("\n--- CHƯƠNG TRÌNH ATM ---")
    print("1. Xem số dư")
    print("2. Rút tiền")
    print("3. Nạp tiền")
    print("4. Thoát")
    print("------------------------") 
def check_balance():  # Hàm kiểm tra số dư
    print(f"Số dư hiện tại của bạn là: {balance:,} VNĐ")
def withdraw_money(): # Hàm rút tiền
    global balance
    amount = int(input("Nhập số tiền muốn rút: "))
    if amount <= 0:
        print("Số tiền không hợp lệ!")
    elif amount > balance:
        print("Số dư không đủ!")
    else:
        balance -= amount
        print(f"Bạn đã rút {amount:,} VNĐ. Số dư còn lại: {balance:,} VNĐ") 
def deposit_money(): # Hàm nạp tiền
    global balance
    amount = int(input("Nhập số tiền muốn nạp: "))
    if amount <= 0:
        print("Số tiền không hợp lệ!")
    else:
        balance += amount
        print(f"Bạn đã nạp {amount:,} VNĐ. Số dư hiện tại: {balance:,} VNĐ")
while True:
    display_menu()
    choice = input("Chọn chức năng (1-4): ")
    if choice == "1":
        check_balance()
    elif choice == "2":
        withdraw_money()
    elif choice == "3":
        deposit_money()
    elif choice == "4":
        print("Cảm ơn bạn đã sử dụng chương trình ATM. Tạm biệt!")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
