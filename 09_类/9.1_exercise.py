# 9-1
class Restaurant():
    """创建一个餐厅的类"""
    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant's name is " + self.restaurant_name + ".")
        print("The cuisine type is " + self.cuisine_type + '.')

    def open_restaurant(self):
        print("The restaurant is open.")

restaurant = Restaurant('Tanko', 'Chinese food')
restaurant.describe_restaurant()
restaurant.open_restaurant()



# 9-2
restaurant_1 = Restaurant('Qilli', 'Mexcican')
restaurant_2 = Restaurant('Macion', 'Japan')
restaurant_3 = Restaurant('Elien', 'Japn')
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()



