# # 8-3
# def make_skirt(size, info):
#     print("The size of the shirt is " + str(size) + ".")
#     print("The text is " + info + ".")
#
#
# # 8-4
# def new_make_skirt(size='L'):
#     if size == 'L' or size == 'M':
#         print("The size is " + size + ", " + "and the information is 'I love Python'.")
#     else:
#         print("The size is " + size + ", " + "and the information is 'I love SQL.'")
#
# new_make_skirt('L')


# 8-5
def describe_city(city_name='Tokyo', country='Japan'):
    print(city_name.title() + " is in " + country.title() + '.')

describe_city('Shanghai', 'China')
describe_city()
