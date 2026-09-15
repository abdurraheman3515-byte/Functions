'''
create a user defined function to perform following task
   electricity units of 5 consumers are given to the function      (argument) in    the form of a dictionary
   calculate the bill amount of each consumer and return it 
   in the form of a list
  {"abdullah":120,"Ali":250.................}
   follow the below criteria to calculate the bill amounts
   a: all consumers must pay a fixed amount of 100
   b: for each unit between 1 to 200, the electricity rate will be rs 3 per unit
   c: for each unit between 201 to 300, the rate should be rs 4 per unit
   d: for each unit between 301 to 400, rate should be rs 5 per unit
   e: d: for each unit between 401 to 500, rate should be rs 6 per unit
   f: for all units above 500, rate should be rs 7 per unit
   '''


def bill_amount_calculate(user):
    bills = []

    for name, units in user.items():

        # Fixed amount
        bill = 100

        if units <= 200:
            bill += units * 3

        elif units <= 300:
            bill += (200*3) + ((units - 200)*4)
        elif units <= 400:
            bill += (200*3) + (100*4) + ((units-300)*5)
        elif units <= 500:
            bill += (200*3) + (100*4) + (100*5) + ((units-400)*6)
        else:
            bill += (200*3) + (100*4) + (100*5) + (100*6) + ((units-500)*7)
        bills.append([name, bill])

    return bills


user = {"abdullah": 120,
        "Ali": 250,
        "sahil": 350,
        "sawez": 450,
        "Aatif": 550}

a = bill_amount_calculate(user)
print(a)
