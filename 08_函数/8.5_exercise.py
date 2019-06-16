# 8-12
def make_sandwiches(*toppings):
    print("\nMaking sandwiches with the following toppings: ")
    for topping in toppings:
        print("-" + topping)


make_sandwiches('meat')
make_sandwiches('egg', 'sugar', 'green pepper', 'bacon')



# 8-13
def build_profile(first, last, **user_info):
    profile = {}
    profile[first] = first
    profile[last] = last

    for key, value in user_info.items():
        profile[key] = value

    return profile

user_profile = build_profile('Tracy', 'Yao', location='Shanghai',
                             graduate_school='Southwestern University of Economics and Finance')
print(user_profile)


