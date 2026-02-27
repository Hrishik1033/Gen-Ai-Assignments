def apply_discount(price,discount_percent=5):#This ensures that if the discount percent is not give, default is 5%
    if discount_percent>60:
        discount_percent = 60
    final_price = price*(1-discount_percent/100)
    print(f"The discounted price is {final_price}")
apply_discount(1000,10)
apply_discount(500)

    