orders = [100,2500,800,1750,3000]
final_amount = 0
total_revenue = 0
for order_amount in orders:
    if order_amount>=2000:
        final_amount = order_amount-0.15*order_amount
        print("Initial amount = ",order_amount," discount% = 15 final_amount = ",final_amount)
    elif order_amount>=1500 and order_amount<2000:
        final_amount=order_amount-0.1*order_amount
        print("Initial amount = ",order_amount," discount% = 10 final_amount = ",final_amount)
    elif order_amount>=1000 and order_amount<1500:
        final_amount=order_amount-0.07*order_amount
        print("Initial amount = ",order_amount," discount% = 7 final_amount = ",final_amount)
    else:
        final_amount = order_amount
        print("Initial amount = ",order_amount," discount% = 0 final_amount = ",final_amount)
    total_revenue+=final_amount
    final_amount = 0
print("The total revenue is = ",total_revenue)