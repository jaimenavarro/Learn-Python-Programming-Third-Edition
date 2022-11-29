# coupons.py
customers = [
    dict(id=1, total=200, coupon_code='F20'),
    dict(id=2, total=150, coupon_code='P30'),
    dict(id=3, total=100, coupon_code='P50'),
    dict(id=4, total=110, coupon_code='F15'),
]

discount = dict(
    F20=(0, 20),
    P30=(0.3, 0),
    P50=(0.5, 0),
    F15=(0, 15),
)

print(type(customers))
print(type(discount))

for customer in customers:
    code = customer['coupon_code']
    percent, fixed = discount.get(code, (0, 0))
    customer['discount'] = customer['total'] * percent + fixed
    print(customer)
