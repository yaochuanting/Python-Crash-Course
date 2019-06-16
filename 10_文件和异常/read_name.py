def dog_cat_name(filename):
    """打印猫和狗的名字"""
    try:
        with open(filename, 'r') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, then file " + filename + " does not exist.")
    else:
        words = contents.split()
        for word in words:
            print(word)
