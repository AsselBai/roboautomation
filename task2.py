'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

import sys
#cNumber is a number of different coins
def MinNumberOfCoins(coins, cNumber, Value):
    #table[i] will store the minimal number of coins required for i value
    #table[r] will have results
    table=[0 for i in range(Value+1)]
    #base case - if given Value is 0
    table[0]=0
    #Initialize all table Value as Infinite
    for i in range(1, Value+1):
        table[i] = sys.maxsize

    #Compute minimum coins required
    #for all values from 0 to value
    for i in range(1, Value+1):
        
        # Go through all coins smaller than i
        for j in range(cNumber):
            if (coins[j]<=i):
                subresult=table[i-coins[j]]
                if(subresult!=sys.maxsize and subresult+1<table[i]):
                    table[i]=subresult+1
    if table[Value]==sys.maxsize:
        return -1
    return table[Value]
# test
coins=[1,5,10,20,50,100]
cNumber= len(coins)
Value = int(input("Please, enter a number value: "))
# max3size is equal to 9223372036854775807
if Value>=sys.max3size:
   print("The entered number exeeds the maximum allowed value. Please, try again")

print("Minimum number of coins is: ", MinNumberOfCoins(coins,cNumber, Value))



