# 修改列表元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)


# 在列表中添加元素
# 在列表末尾添加元素 append()
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append("ducati")
print(motorcycles)

# 创建空列表，在其中添加元素
motorcycles = []
motorcycles.append("honda")
motorcycles.append("yamaha")
motorcycles.append("suzuki")
print(motorcycles)

# 在列表中插入元素 insert()
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)


# 在列表中删除元素 del
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# 使用pop方法删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
poped_motorcycle = motorcycles.pop()
print(motorcycles)
print(poped_motorcycle)

# 指出最后一辆购买的摩托车
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(last_owned)
print("The last motorcycle I owned was a " + last_owned.title() + ".")

# 弹出列表中任何位置的元素
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned + ".")
