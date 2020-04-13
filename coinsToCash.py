# Create a function that will take all your coins and convert it to the cash amount.
def calc_dollars(**coins):
    coin_stuff = coins.items()
    for coinType, numberOfCoins in coin_stuff: 
        if coinType == "pennies":
            pennyAmount = numberOfCoins/100
           
        if coinType == "nickels": 
            nickelAmount = numberOfCoins * .05
           
        if coinType == "dimes": 
            dimeAmount = numberOfCoins * .1
           
        if coinType == "quarters": 
            quarterAmount = numberOfCoins / 4
            
    sum = (pennyAmount+nickelAmount+dimeAmount+quarterAmount)
    print(sum)

calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)
