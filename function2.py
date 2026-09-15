def amount_discount(price,qty):
    amount=price*qty
    if amount>=10000:
        discount=0.1
    elif amount>=5000:
        discount=0.05
    else:
        discount=0
    return amount-amount*discount

p=amount_discount(1500,10)
print(p)

p=amount_discount(200,5)
print(p)


