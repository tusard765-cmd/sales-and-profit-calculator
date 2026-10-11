print("---- Sales & Profit Calculator ----")

buy_price = float(input("Enter the buy price: "))
sell_price = float(input("Enter the sell price: "))
quantity = int(input("Enter the quantity: "))

if buy_price < 0 or sell_price < 0 or quantity < 0:
    print("Price and quantity cannot be negative.")
else:
    profit = (sell_price - buy_price) * quantity

    if profit > 0:
        print(f"Profit: Rs. {profit:.2f}")
    elif profit < 0:
        print(f"Loss: Rs. {-profit:.2f}")
    else:
        print("No profit, no loss.")
