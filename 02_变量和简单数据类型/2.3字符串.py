# 修改单词大小写 title()首字母大写
name = "ada lovelace"
print(name.title())

# 全部大写
print(name.upper())

# 全部小写
print(name.lower())


# 合并拼接字符串
first_name = "Tracy"
last_name = "YAO"
full_name = first_name + " " + last_name
message = "Hello, " + full_name
print(message)


# 制表符
print("Python")
print("\tPython")


# 换行符
print("Languages:\nPython\nC\nJavaScript")

# 制表符&换行符
print("Languages:\n\tPython\n\tC\n\tJavaScript")


# 删除空白
# rstrip()删除末尾的空白
favorite_language_1 = 'Python '
print(favorite_language_1)
print(favorite_language_1.rstrip())

favorite_language_2 = ' Python '
print(favorite_language_2.lstrip())
print(favorite_language_2.strip())

# 单引号和双引号
message = "One of Python's strength is its diverse community"
print(message)

