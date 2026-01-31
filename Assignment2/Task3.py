
print("Choice options:\n1)Add items\n2)View all orders and discounts\nq)Quit")
choice = input("Enter your choice: ")
prices = []
discount_price = []
while(choice!='q'):
    
    if(choice == '1'):
        choice = input("Item price: ")
        prices.append( int(choice))
        order_amount = int(choice)
        if order_amount>=2000:
            final_amount = order_amount-0.15*order_amount
            discount_price.append(final_amount)

        elif order_amount>=1500 and order_amount<2000:
            final_amount=order_amount-0.1*order_amount
            discount_price.append(final_amount)

        elif order_amount>=1000 and order_amount<1500:
            final_amount=order_amount-0.07*order_amount
            discount_price.append(final_amount)

        else:
            final_amount = order_amount
            discount_price.append(final_amount)
        
    elif choice == '2':
        print("The ordered list is: ",prices,"\nThe discounted list is: ",discount_price)
    else:
        print("Wrong choice")
        continue
    choice = input("Enter your choice: ")
    