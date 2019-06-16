# 8-9
def show_magicians(names):
    for name in names:
        print(name.title())

magicians = ['rita', 'ivy', 'tom', 'Rajh']
show_magicians(magicians)



# 8-10
def show_magicians(names):
    for i in range(0, 4):
        names[i] = "the Great " + names[i]


magicians = ['rita', 'ivy', 'tom', 'Rajh']
show_magicians(magicians)
print(magicians)




# 8-11
def show_magicians(names):
    for i in range(0, 4):
        names[i] = "the Great " + names[i]


magicians = ['rita', 'ivy', 'tom', 'Rajh']
new_magicians = magicians[:]
show_magicians(new_magicians)
print(new_magicians)
print(magicians)
