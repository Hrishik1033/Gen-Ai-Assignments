try:
    order_amount = int(input("Enter total order amount: "))

    if order_amount>=2000:
        order_amount-=0.15*order_amount
    elif order_amount>=1500 and order_amount<2000:
        order_amount-=0.1*order_amount
    elif order_amount>=1000 and order_amount<1500:
        order_amount-=0.07*order_amount
    else:
        order_amount = order_amount
    print("Your final order amount is = ",order_amount)
except:
    print("Not a valid input")