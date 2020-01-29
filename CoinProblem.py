import random
import CoinCase
import sys

# creat coin case
CC = CoinCase.CoinCase()
CC.caseContains()

# create withdrawal
withdrawAmount = random.randint(0, 100)
print('Try to withdraw ' + str(withdrawAmount))

# get Modulus 5 and 10
mod5 = withdrawAmount % 5
mod10 = withdrawAmount % 10

# exact amount is possible boolean
EAB = True

# this function returns EAB ture or false


def checkEAB():
    # is there enough to withdraw
    if withdrawAmount > CC.total:
        print('Unable to withdraw ' + str(withdrawAmount) +
              ' cents. NOT enough money in the piggy bank.')
        sys.exit()
    else:
        # mod 10 check
        if mod10 == 0:
            # mod 5 check
            if mod5 == 0:
                EAB = True
            else:
                # pennies check
                if CC.pennies >= mod5:
                    EAB = True
                else:
                    EAB = False
        else:
            # mod 5 check
            if mod5 == 0:
                # pennies check
                if CC.pennies >= 5:
                    EAB = True
                else:
                    EAB = False
            else:
                # pennies check
                if CC.pennies >= mod5:
                    EAB = True
                else:
                    EAB = False


checkEAB()

# holding numbers and array while adding up coins
holdNum = 0
holdArry = []
diff = withdrawAmount-holdNum

# change until EAB is true
while not EAB:
    withdrawAmount += 1
    print(withdrawAmount)
    checkEAB()
    print(EAB)

# get coins
if EAB:
    while diff > 0:
        if (CC.quarters > 0 and diff >= 25) or (CC.quarters > 0 and CC.pennies == 0 and CC.nickels == 0 and CC.dimes == 0) or (CC.quarters > 0 and (CC.dtotal + CC.ntotal + CC.ptotal < diff)):
            CC.removeCoin('quarter')
            holdNum += 25
            holdArry.append('quarter')
            diff = withdrawAmount-holdNum
        elif (CC.dimes > 0 and diff >= 10) or (CC.dimes > 0 and CC.pennies == 0 and CC.nickels == 0) or (CC.dimes > 0 and (CC.ntotal + CC.ptotal < diff)):
            CC.removeCoin('dime')
            holdNum += 10
            holdArry.append('dime')
            diff = withdrawAmount-holdNum
        elif (CC.nickels > 0 and diff >= 5) or (CC.nickels > 0 and CC.pennies == 0) or (CC.nickels > 0 and (CC.ptotal < diff)):
            CC.removeCoin('nickel')
            holdNum += 5
            holdArry.append('nickel')
            diff = withdrawAmount-holdNum
        elif CC.pennies > 0:
            CC.removeCoin('penny')
            holdNum += 1
            holdArry.append('penny')
            diff = withdrawAmount-holdNum

# print coins
for item in holdArry:
    print(item)
