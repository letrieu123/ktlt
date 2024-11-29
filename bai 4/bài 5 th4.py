print ("sinh vien:Le Thanh Khanh Trieu MSV:235752021610117")
ds = input('Danh sách: ')
'''Sử dụng hàm split()để chia chuỗi thành danh sách
với các phần tử cách nhau bởi dấu trống hoặc tab'''
elements=ds.split()
#in ra danh sách theo thứ tự ngược lại
print("dãy theo thứ tự ngược lại là:", ' '.join(elements[::-1]))

