# 将名字列表传递给一个函数
def greet_users(names):
    """向列表中每个人发送问候"""
    for name in names:
        msg = "Hello, " + name.title() + '!'
        print(msg)

user_names = ['kitty', 'jolin', 'kevin', 'lisa']
greet_users(user_names)



# 在函数中修改列表
def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都把打印好的设计增加到列表completed_models中
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # 模拟根据设计打印过程
        print("Printing models: " + current_design)
        # 将打印好的设计计入列表completed_models
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的模型"""
    print("The following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pedent', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


