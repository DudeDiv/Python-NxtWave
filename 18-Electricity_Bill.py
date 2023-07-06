#Write a program to calculate the electricity bill for a household, based on the units of electricity the household consumed.
#The price for unit varies based on the slab. The charges per unit for different slabs are as mentioned below:
#For the first 50 units (0-50), the charge is 2/unit
#For the next 100 units (51-150), the charge is 3/unit
#For the next 100 units (151-250), the charge is 5/unit
#For above 250 units (251 and above), the charge is 8/unit
#Apart from these charges, there is also an additional surcharge of 20% on the total amount is added to the bill.
units = int(input())

if(units>=0 and units<=50):
    total_bill = 2*units
if(units>50 and units<=150):
    total_bill = 2*50 + 3*(units-50)
if(units>150 and units<=250):
    total_bill = 2*50 + 100*3 + 5*(units - 150)
if(units>250):
    total_bill = 2*50 + 100*3 + 100*5 + 8*(units-250)
grand_total = total_bill + (20/100)*total_bill
print(grand_total)
