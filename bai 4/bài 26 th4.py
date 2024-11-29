print("sinh vien:le thanh khanh trieu MSV:235752021610117")
# Khởi tạo số dư tài khoản ban đầu
balance = 0
n = int(input("Nhập số lượng giao dịch: "))
# Duyệt qua từng giao dịch và tính toán số dư
for _ in range(n):
    transaction = input("Nhập giao dịch (D/W <số tiền>): ").split()
    action = transaction[0]  # Lấy loại giao dịch (D hoặc W)
    amount = int(transaction[1])  # Lấy số tiền giao dịch

    if action == "D":  # Nếu giao dịch là gửi tiền
        balance += amount
    elif action == "W":  # Nếu giao dịch là rút tiền
        balance -= amount
print(balance)
