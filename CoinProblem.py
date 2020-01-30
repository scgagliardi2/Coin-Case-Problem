import random
import CoinCase
import sys

# create coin case
CC = CoinCase.CoinCase()
# print case contents
CC.caseContains()

# create withdrawal
withdrawAmount = random.randint(0, 100)
# print withdrawal amount
print('Try to withdraw ' + str(withdrawAmount))

# get Moduli
mod5 = withdrawAmount % 5
mod10 = withdrawAmount % 10
mod25 = withdrawAmount % 25


def findPerfectSolution():  # find solution when perfect solution is an option
    global withdrawAmount
    global mod5
    global mod10
    global mod25
    holdArray = []
    solutionFound = False
    while not solutionFound:
        if withdrawAmount > 0:
            if mod25 != 0 or CC.quarters == 0:
                if withdrawAmount >= 50 and CC.quarters > 1:
                    withdrawAmount -= 50
                    holdArray.append('quarter')
                    CC.removeCoin('quarter')
                    holdArray.append('quarter')
                    CC.removeCoin('quarter')
                    mod5 = withdrawAmount % 5
                    mod10 = withdrawAmount % 10
                    mod25 = withdrawAmount % 25
                    continue
                elif withdrawAmount >= 35 and CC.dimes > 0 and CC.quarters > 0:
                    withdrawAmount -= 35
                    holdArray.append('dime')
                    CC.removeCoin('dime')
                    holdArray.append('quarter')
                    CC.removeCoin('quarter')
                    mod5 = withdrawAmount % 5
                    mod10 = withdrawAmount % 10
                    mod25 = withdrawAmount % 25
                    continue
                elif withdrawAmount >= 30 and CC.nickels > 0 and CC.quarters > 0:
                    withdrawAmount -= 30
                    holdArray.append('nickel')
                    CC.removeCoin('nickel')
                    holdArray.append('quarter')
                    CC.removeCoin('quarter')
                    mod5 = withdrawAmount % 5
                    mod10 = withdrawAmount % 10
                    mod25 = withdrawAmount % 25
                    continue
                else:
                    if mod10 != 0 or CC.dimes == 0:
                        if mod5 != 0 or CC.nickels == 0:
                            withdrawAmount -= 1
                            holdArray.append('penny')
                            mod5 = withdrawAmount % 5
                            mod10 = withdrawAmount % 10
                            mod25 = withdrawAmount % 25
                            continue
                        else:
                            withdrawAmount -= 5
                            holdArray.append('nickel')
                            CC.removeCoin('nickel')
                            mod5 = withdrawAmount % 5
                            mod10 = withdrawAmount % 10
                            mod25 = withdrawAmount % 25
                            continue
                    else:
                        withdrawAmount -= 10
                        holdArray.append('dime')
                        CC.removeCoin('dime')
                        mod5 = withdrawAmount % 5
                        mod10 = withdrawAmount % 10
                        mod25 = withdrawAmount % 25
                        continue
            else:
                withdrawAmount -= 25
                holdArray.append('quarter')
                CC.removeCoin('quarter')
                mod5 = withdrawAmount % 5
                mod10 = withdrawAmount % 10
                mod25 = withdrawAmount % 25
                continue
        else:
            solutionFound = True
    return [solutionFound, holdArray]


def findImperfectSolution():  # find solution when perfect solution is not an option
    global withdrawAmount
    global mod5
    global mod10
    global mod25
    # holding numbers and array while adding up coins
    holdNum = 0
    holdArry = []
    diff = withdrawAmount-holdNum
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
        return [True, holdArry]
    else:
        return [False, holdArry]


# boolean stating whether or not an exact amount is possible
EAB = True


def checkForPerfectSolution():  # this function returns EAB ture or false
    global EAB
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
                if CC.pennies >= 5 or CC.nickels > 1:
                    EAB = True
                else:
                    EAB = False
            else:
                # pennies check
                if CC.pennies >= mod5:
                    EAB = True
                else:
                    EAB = False


# run the check
checkForPerfectSolution()

if EAB:
    solutionFound = findPerfectSolution()
else:
    # add one to withdrawal amount until EAB is true, if it isn't already
    while not EAB:
        withdrawAmount += 1
        mod5 = withdrawAmount % 5
        mod10 = withdrawAmount % 10
        mod25 = withdrawAmount % 25
        checkForPerfectSolution()
    # get coins if true
    solutionFound = findImperfectSolution()


if solutionFound[0]:
    for item in solutionFound[1]:
        print(item)
