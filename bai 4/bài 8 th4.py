print("sinh vien:Le Thanh Khanh Trieu Mssv 235752021610117")
input_str = input("Nhập dãy các từ: ")
words = input_str.split()
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Từ dài nhất là:")
for word in longest_words:
    print(word)
