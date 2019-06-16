#7-8
sandwich_orders = ['cake sandwich', 'chicken sandwich', 'ham sandwich', 'roast pork sandwich']
finished_orders = []
while sandwich_orders:
    for sandwich_order in sandwich_orders:
        finished_order = sandwich_orders.pop()
        finished_orders.append(finished_order)

        print("I made your " + finished_order + ".")

print("\nI made some sandwiches: ")

for finished_order in finished_orders:
    print("\t" + finished_order)




# 7-9
sandwich_orders = ['cake sandwich', 'pastrami', 'chicken sandwich', 'ham sandwich', 'roast pork sandwich', 'pastrami']
print(sandwich_orders)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)




# 7-10
responses = {}
polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Would you like to let another people respond?(yea/no) ")

    if repeat == 'no':
        polling_active = False

print("\n--------Poll Results---------")
for name, response in responses.items():
    print(name.title() + " would like to go to " + response + ".")
