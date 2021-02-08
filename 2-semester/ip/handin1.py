"""
HANDIN 1 (down payment)

This handin is done by (study ids and names of up to three students):

    201500000 <student name>
    201600000 <student name> 
    201400000 <student name>

Reflection upon solution:

    <For at løse denne opgave har jeg først valgt at definere en `term`. Det har jeg gjort
    fordi jeg senere laver en løkke til at bruge min beregning, som jeg definere som
    `calculation`.  
    Det svære i denne opgave var at finde den korrekte måde at udregne det på. Her fik jeg inspiration
    fra siden https://pocketsense.com/calculate-number-years-required-pay-off-outstanding-loans-15522.html
    til selve udregningen.
    I stedet for at bruge en while bruge jeg en for løkke. Det giver mig det ønskede resultat.
    Desuden bruge jeg pakkerne numpy og pandas til at bruge nogle af deres funktionaliteter
    til udregninger og til at lave en data frame.
    En forbedring som jeg kunne tænke mig var at fjerne term i min kode. Det burde kunne laves uden, så
    jeg ikke skal definere antal term, men koden virker og jeg fik ikke formådet at lave det uden.
    Desuden laver jeg en break for vores P (principal) for 0, så inden den kommer under nul, så
    skal vi stoppe løkken. Det kunne også forbedres, så man enten betaler resten ud.>
"""

import numpy as np
import pandas as pd

term = 180
P = float(input("Loan amount \n"))
rent = float(input("Your interest rent \n"))
mp = float(input('Your monthly payment \n'))

def calculation(P, mp, interest_rate = rent):
    interest_paid = np.floor(((rent/12) * P) * 100) / 100
    principal_paid = np.round(mp - interest_paid, 2)
    new_balance = np.round(P - principal_paid, 2)
    return(mp, interest_paid, principal_paid, new_balance)

payment_list = []

for n in range(1, term + 1):
    mp,i_paid,p_paid,new_p = calculation(P, mp)
    if (new_p <= 0): break
    payment_list.append([n, new_p])
    P = np.round(new_p, 2)
column_names = ['Month', 'Balance']

payment_table = pd.DataFrame(payment_list, columns = column_names)
print(payment_table)
...

