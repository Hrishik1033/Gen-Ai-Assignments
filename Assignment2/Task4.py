daily =[200,150,0,400,50,-1,300]
total_sales = 0
for value in daily:
    if value == -1:
        print("Corrupted....")
        break
    elif value == 0:
        print("No sales")
        continue
    elif value>0:
        total_sales+=value
        print(total_sales)

print("Total sales = ",total_sales)