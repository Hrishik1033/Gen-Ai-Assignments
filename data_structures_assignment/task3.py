price_dict={"Juice":40,"Momo":30,"Chips":10,"Chocolate":25,"Bag":100,"Bottle":20}
print(price_dict)
price_dict.update({"Copy":20})
print(price_dict)
price_dict.update({"Juice":30})
print(price_dict)
remove_pdt1 = 'Momo'
remove_pdt2 = 'Laptop'
if(remove_pdt1 in price_dict):
    price_dict.pop(remove_pdt1)
else:
    print("The item dosent exist")
print(price_dict)

prices = price_dict.values()
total = 0
for i in prices:
    total+=i
print(total)
