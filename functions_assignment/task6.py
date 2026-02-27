def greater(price):
    if price>300:
        return price
def lesser(price):
    if price<=300:
        return price

def process_prices(prices):
    if isinstance(prices,list):
        price_with_discount = list(map(lambda x:x*(1-10/100),prices))
        above_300 = list(filter(greater,price_with_discount))
        less_300 = list(filter(lesser,price_with_discount))
        print(f"Discounted prices: {price_with_discount}\nPrices above 300: {above_300}\nPrices below 300: {less_300} ")

    else:
        print("Wrong input type..")
prices = [100,500,900,50,750]
process_prices(prices)