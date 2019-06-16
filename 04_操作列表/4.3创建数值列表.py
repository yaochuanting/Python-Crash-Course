# 使用range()函数生成数字
for values in range(1,5):
    print(values)

# 使用range创建数字列表
numbers = list(range(1,6))
print(numbers)

# range()还可设置步长
numbers = list(range(2,11,2))
print(numbers)

# 创建一个列表包含前十个整数的平方
squares = []
for value in range (1,11):
    square = value ** 2
    squares.append(square)
print(squares)

# 对数字列表执行简单的计算
digits = list(range(0,10))
print(min(digits))
print(max(digits))
print(sum(digits))

# 列表解析
squares = [value**2 for value in range(1,11)]
print(squares)