prices = [100,250,400,1200,50,2000,850]
prices_with_gst = list(map(lambda x:x*(1+18/100),prices))
print(f"Original Prices: {prices}\nPrices after gst: {prices_with_gst}")