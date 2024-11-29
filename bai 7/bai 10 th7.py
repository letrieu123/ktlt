print("sinh vien:le thanh khanh trieu MSV:235752021610117")
def find_longest_words(text):
    words = text.split()
    cleaned_words = [word.strip(".,!?;:()[]{}\"'") for word in words]
    max_length = max(len(word) for word in cleaned_words)
    longest_words = [word for word in cleaned_words if len(word) == max_length]
    return longest_words
text = """
PyCharm là một phần mềm được phát triển bởi JetBrains, cung cấp các công 
cụ cần thiết giúp các lập trình viên Python tăng năng suất làm việc.
"""
longest_words = find_longest_words(text)
print("Những từ dài nhất trong văn bản là:", longest_words)
