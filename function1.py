 #defination of function
def create_dictionary(Pnames,prices):


    my_products=dict()
    if len(Pnames)!=len(prices):
        print("Pname and price length is not match ")
    else:
        for i in range(len(Pnames)):
            my_products[Pnames[i]]=prices[i]
    return my_products

    

#Call function
p=create_dictionary(["keyboard","Mouse","printer"],["800","250","12000"])
print(p)





























