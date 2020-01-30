import random
import CoinCase
import sys

# create coin case
# case also dreats a withdrawal amount and mod 5, 10, and 25
CC = CoinCase.CoinCase()
# print case contents
CC.caseContains()

# print withdrawal amount
print('Try to withdraw ' + str(CC.withdraw))


def getCoins():  # find solution when perfect solution is an option
    holdArray = []
    solutionFound = False
    while not solutionFound:
        if CC.withdraw > 0:
            if CC.mod25 != 0 or CC.quarters == 0:
                if CC.withdraw >= 50 and CC.quarters > 1:
                    CC.withdraw -= 50
                    holdArray.append('quarter')
                    CC.removeCoin('quarter')
                    holdArray.append('quarter')
                    CC.removeCoin('quarter')
                    CC.getMod(CC.withdraw)
                    continue
                elif CC.withdraw >= 35 and CC.dimes > 0 and CC.quarters > 0 and (checkForPerfectSolution(CC.withdraw - 35)):
                    CC.withdraw -= 35
                    holdArray.append('dime')
                    CC.removeCoin('dime')
                    holdArray.append('quarter')
                    CC.removeCoin('quarter')
                    CC.getMod(CC.withdraw)
                    continue
                elif CC.withdraw >= 30 and CC.nickels > 0 and CC.quarters > 0 and (checkForPerfectSolution(CC.withdraw - 30)):
                    CC.withdraw -= 30
                    holdArray.append('nickel')
                    CC.removeCoin('nickel')
                    holdArray.append('quarter')
                    CC.removeCoin('quarter')
                    CC.getMod(CC.withdraw)
                    continue
                else:
                    if CC.mod10 != 0 or CC.dimes == 0:
                        if CC.mod5 != 0 or CC.nickels == 0:
                            CC.withdraw -= 1
                            holdArray.append('penny')
                            CC.getMod(CC.withdraw)
                            continue
                        else:
                            CC.withdraw -= 5
                            holdArray.append('nickel')
                            CC.removeCoin('nickel')
                            CC.getMod(CC.withdraw)
                            continue
                    else:
                        CC.withdraw -= 10
                        holdArray.append('dime')
                        CC.removeCoin('dime')
                        CC.getMod(CC.withdraw)
                        continue
            else:
                CC.withdraw -= 25
                holdArray.append('quarter')
                CC.removeCoin('quarter')
                CC.getMod(CC.withdraw)
                continue
        else:
            solutionFound = True
    return [solutionFound, holdArray]


# boolean stating whether or not an exact amount is possible
EAB = True


def checkForPerfectSolution(wA):  # this function returns EAB ture or false
    amount = wA
    # is there enough to withdraw
    if amount > CC.total:
        print('Unable to withdraw ' + str(CC.withdraw) +
              ' cents. NOT enough money in the piggy bank.')
        sys.exit()
    else:
        # mod 5, are there enough pennies
        if CC.pennies >= CC.mod5:
            # subtract out pennies if needed
            amount = amount - CC.mod5
            CC.getMod(amount)
            # check mod 25
            if CC.mod25 == 0:
                # are there enough quarters
                if (amount/25) <= CC.quarters:
                    return True
                # are there enough dimes and nickels
                else:
                    amount = amount - (CC.quarters)*25
                    if amount < (CC.dtotal + CC.nickels + CC.pennies):
                        return True
                    else:
                        return False
            elif CC.mod10 == 0:
                # can I use two quarters
                while amount >= 50:
                    if (amount-50) < (CC.qtotal + CC.dtotal + CC.ntotal + CC.ptotal) and CC.quarters >= 2:
                        amount = amount - 50
                        CC.removeCoin('quarter')
                        CC.removeCoin('quarter')
                    else:
                        return False
                # can I use 1 quarter and one dime
                while amount >= 35:
                    if (amount-35) < (CC.qtotal + CC.dtotal + CC.ntotal + CC.ptotal):
                        amount = amount - 35
                    else:
                        return False
                # can I use 1 quarter and one nickel
                while amount >= 30:
                    if (amount-30) < (CC.qtotal + CC.dtotal + CC.ntotal + CC.ptotal):
                        amount = amount - 30
                    else:
                        return False
                # can I use 1 quarter
                while amount >= 25:
                    if (amount-25) < (CC.qtotal + CC.dtotal + CC.ntotal + CC.ptotal):
                        amount = amount - 30
                    else:
                        return False
            elif CC.mod5 == 0:
        else:
            return False


# run the check
EAB = checkForPerfectSolution(CC.withdraw)
CC.getMod(CC.withdraw)

if EAB:
    solutionFound = getCoins()
else:
    # add one to withdrawal amount until EAB is true, if it isn't already
    while not EAB:
        CC.withdraw += 1
        CC.getMod(CC.withdraw)
        EAB = checkForPerfectSolution(CC.withdraw)
    # get coins if true
    solutionFound = getCoins()


if solutionFound[0]:
    for item in solutionFound[1]:
        print(item)
