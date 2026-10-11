print("----sales & profit----")
buy_price = float(input("Enter the buy price: "))
sell_price = float(input("Enter the sell price: "))
quantity = int(input("Enter the quantity: "))

profit = (sell_price - buy_price) * quantity
if profit > 0:
    print(f"Profit: {profit:.2f}")
else:
    print("No profit generated.")

