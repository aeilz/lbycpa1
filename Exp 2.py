import os

monthlyIncome = float(input("Enter monthly income: "))
annualIncome = monthlyIncome*12

def taxCalc(annualIncome):
    if annualIncome <= 250000:
        return annualIncome*0 #0% Tax Rate
    elif annualIncome <= 400000:
        return annualIncome*.15 #15% Tax Rate
    elif annualIncome <= 800000:
        return annualIncome*.20+22500 #20% Tax Rate
    elif annualIncome <= 2000000:
        return annualIncome*.25+102500 #25% Tax Rate
    elif annualIncome <= 8000000:
        return annualIncome*.30+402500 #30% Tax Rate
    else:
        return annualIncome*.35+2205000

monthlyTax = taxCalc(annualIncome)/12
annualTax = taxCalc(annualIncome)

monthlyNetPay = monthlyIncome-monthlyTax
annualNetPay = annualIncome-annualTax

print ("\nYour monthly income is: {}".format (monthlyIncome))
print ("Your annual income is: {}".format(annualIncome))

print ("\nYour monthly tax is: {}".format (monthlyTax))
print ("Your annual tax is: {}".format(annualTax))

print ("\nYour monthly net pay: {}".format(monthlyNetPay))
print ("Your annual net pay is: {}".format(annualNetPay))

print("\nThank you for using this program!\n")

os.system("pause")