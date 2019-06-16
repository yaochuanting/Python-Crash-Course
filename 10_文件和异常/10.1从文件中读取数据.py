# 读取整个文件
with open('D:\Python_work\pi.txt') as file_object:
    contents = file_object.read()
    print(contents)




# 逐行读取
file_name = 'D:\Python_work\pi.txt'

with open(file_name) as file_object:
    for line in file_object:
        print(line.rstrip())



# 创建一个包含文件各行内容的列表
filename = 'D:\Python_work\pi.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())




# 使用文件中的内容
filename = 'D:\Python_work\pi.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))




filename = 'D:\Python_work\pi.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))




# 包含一百万位的大型文件
filename = 'D:\Python_work\pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))


# 判断圆周率中是否包含你的生日
filename = 'D:\Python_work\pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million of pi!")
else:
    print("Your birthday does not appears in the first million of pi!")





