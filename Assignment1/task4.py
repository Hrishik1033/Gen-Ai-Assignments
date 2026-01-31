price_dict={"Juice":40,"Momo":30,"Chips":10,"Chocolate":25,"Bag":100}

catalog = [("Juice",40,"Drinks"),("Momo",30,"fast_food"),("Chips",10,"fast_food"),("Chocolate",25,"desert"),("Bag",100,"essentials")]
category_to_products  = {"Drinks":["Juice"],"fast_food":["Momo","Chips"],"desert":["Chocolate"],"essentials":["Bag"]}
temp = 0
store = []
#Looping was essential as i could not figure out any other alternative,
#I first made the values cooresponding to keys of type = list so that i oculd compare the number of items

for key in category_to_products:
    if len(category_to_products[key])>=temp:
        temp = len(category_to_products[key])
        store = category_to_products[key]
print(store)