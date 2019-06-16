# 使用for循环打印数字1~20
numbers = [value for value in range(1,21)]
for number in numbers:
    print(number)

# 创建一个列表包含数字1-1000000，再使用for循环打印
numbers = [value for value in range(1,1000001)]
for number in numbers:
    print(number)

# 计算1-1000000的和
numbers = [value for value in range(1,1000001)]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# 创建1-20的奇数列表 并打印
numbers = [value for value in range(1,21,2)]
for number in numbers:
    print(number)

# 创建包含3-30内能被3整除的数字并打印
numbers = [value*3 for value in range(1,11)]
for number in numbers:
    print(number)

# 创建包含前十个整数的立方并打印
numbers = [value**3 for value in range(1,11)]
for number in numbers:
    print(number)