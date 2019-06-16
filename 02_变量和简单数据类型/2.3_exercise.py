# 将姓名存到一个变量中，并向该用户显示这条消息
name = "Eric"
message = "Hello" + " " + name + "," + " " + "would you like to learn some Python today?"
print(message)

# 调整名字的大小写
name = "tracy yao"
print(name.lower())
print(name.upper())
print(name.title())

# 名言名言
name = "albert einstein"
quote = '"A person who never made a mistake never tried anything new."'
message = name.title() + " " + "once said," + " " + quote
print(message)

# 剔除空白字符
name = "\t\n tracy yao \t\n"
print(name.lstrip())
print(name.rstrip())
print(name.strip().title())