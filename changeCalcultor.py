'''
Patel, Jenisha, 760284
2023/11/1
U3A3f Using Modulus - function
'''

dollar = input("Enter a value less than $5 :")

def change(dollar):
    dollar = float(dollar)
    toonies = dollar // 2
    toonies = int(toonies)
    loonies = dollar - (toonies*2) 
    loonies = loonies // 1 
    loonies = int(loonies)
    quarters = dollar - (toonies*2) - (loonies*1)
    quarters = quarters // 0.25  
    quarters = int(quarters)
    dimes = dollar - (toonies*2) - (loonies*1) - (quarters*0.25)
    dimes = dimes // 0.10
    dimes = int(dimes)
    nickels = dollar - (toonies*2) - (loonies*1) - (quarters*0.25) - (dimes*0.10)
    nickels = nickels // 0.05
    nickels = int(nickels)
    pennies = dollar - (toonies*2) - (loonies*1) - (quarters*0.25) - (dimes*0.10) - (nickels*0.05)
    pennies = pennies / 0.01
    pennies = round(pennies)
    pennies = int(pennies)
    coin_values = (toonies, loonies, quarters, dimes, nickels, pennies)
    coin_values_str = ' '.join(map(str, coin_values))
    print(coin_values_str)

change(dollar)
