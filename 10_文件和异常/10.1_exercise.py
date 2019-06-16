# 10-1
filename = 'learning_python.txt'

with open(filename) as file_object:
    messages = file_object.readlines()

for message in messages:
    print(message.strip())