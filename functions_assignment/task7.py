def add_price(prices_list,price):
    prices_list.append(price)
    return
def get_average_price(prices_list):
    add = 0
    for i in prices_list:
        add+=i
    print(f"The average of all elements: {add/len(prices_list)}")

def get_max_price(prices_list):
    store = prices_list[0]
    for i in prices_list:
        if i >store:
            store = i
    print(f"The max element is: {store}")

prices_list = []
print("1. Add Price\n2. Show average price\n3. Show highest price\nq. Quit")
inp = ''
while(inp!='q'):
    inp = str(input("Enter your choice: "))
    if inp == '1':
        price = input("Enter price: ")
        add_price(prices_list = prices_list,price=price)
    elif inp == '2':
        get_average_price(prices_list=prices_list)

    elif inp == '3':
        get_max_price(prices_list=prices_list)
    
