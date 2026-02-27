cost = float(input("Enter cost: "))
discount = float(input("Enter discount percent: "))
gst = lambda price:price*(1+18/100-discount/100)

print(f"The final cost is: {gst(cost)}")