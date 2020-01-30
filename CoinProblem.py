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
    global EAB
    amount = wA
    # is there enough to withdraw
    if amount > CC.total:
        print('Unable to withdraw ' + str(CC.withdraw) +
              ' cents. NOT enough money in the piggy bank.')
        sys.exit()
    else:
        # mod 10 check
        if CC.mod10 == 0:
            # mod 5 check
            if CC.mod5 == 0:
                EAB = True
            else:
                # pennies check
                if CC.pennies >= CC.mod5:
                    EAB = True
                else:
                    EAB = False
        else:
            # mod 5 check
            if CC.mod5 == 0:
                # pennies check
                if CC.pennies >= 5 or CC.nickels > 1:
                    EAB = True
                else:
                    EAB = False
            else:
                # pennies check
                if CC.pennies >= CC.mod5:
                    EAB = True
                else:
                    EAB = False


# run the check
checkForPerfectSolution(CC.withdraw)

if EAB:
    solutionFound = getCoins()
else:
    # add one to withdrawal amount until EAB is true, if it isn't already
    while not EAB:
        CC.withdraw += 1
        CC.getMod(CC.withdraw)
        checkForPerfectSolution(CC.withdraw)
    # get coins if true
    solutionFound = getCoins()


if solutionFound[0]:
    for item in solutionFound[1]:
        print(item)
