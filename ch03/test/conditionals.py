order_total = int(input())
print("Number: ", order_total)

# classic if/else form
if 0 < order_total < 100:
    discount = 25  # GBP
else:
    discount = 0  # GBP
print(order_total, discount)

# ternary operator
discount = 25 if 0 < order_total < 100 else 0
print(order_total, discount)
