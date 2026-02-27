def greater(price):
    if price>500:
        return price
def lesser(price):
    if price<=500:
        return price

prices = [100,250,400,1200,50,2000,850]
store_greater = list(filter(greater,prices))
store_lesser = list(filter(lesser,prices))
print(f"List of prices greater than 500: {store_greater}\nList of prices lesser than 500: {store_lesser}")