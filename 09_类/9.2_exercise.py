class Restaurant():
    """创建一个餐厅的类"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + ".")
        print("The cuisine type is " + self.cuisine_type + '.')

    def open_restaurant(self):
        print("The restaurant is open.")

    def describe_num_served(self):
        print("The restaurant has served " + str(self.number_served) + ' people.')

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, increment):
        self.number_served += increment



# 创建restaurant实例，打印有多少人在这家餐厅就餐过
restaurant = Restaurant('MinTai', 'western food')
print(str(restaurant.number_served) + " people served in this restaurant.")

restaurant.set_number_served(15)
restaurant.describe_num_served()

restaurant.increment_number_served(20)
restaurant.describe_num_served()