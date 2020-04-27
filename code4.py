print("***tax Program***")
price=float(input("how much did you pay?: "))
if price>=1.00:
    tax=0.07
    print('tax rate is:'+str(tax))
else: 
    tax=0
    print('tax rate is:'+str(tax))
