products = ['juice','chips','chocolate','bag','bottle','copy']
categories_set = {'drinkable','eatables','stationaries'}
categories_set.add('school')
print(categories_set)
categories_set.add('drinkable')
print(categories_set)

store_category = 'eatables'
if(store_category in categories_set):
    print(True)
else:
    print(False)