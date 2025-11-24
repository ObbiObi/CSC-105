#Compound Interest Loops
#Compound Interest Function
def compound_interest(intDeposit, fltMonthlyRate, intMonths, fltGoal):
    #Loop to calculate compound interest over specified months
    for i in range(intMonths):
        intInterest = intDeposit * fltMonthlyRate/100
        intDeposit = intDeposit + intInterest
        print(f"Month: {i+1} Account Balance is: $ {intDeposit:,.2f}")
    #Loop to calculate months needed to reach goal amount
    if fltGoal > intDeposit:
        while True:
            intInterest = intDeposit * fltMonthlyRate/100
            intDeposit = intDeposit + intInterest
            intMonths += 1
            if intDeposit >= fltGoal:
                print(f"It will take {intMonths} months to reach your goal of ${fltGoal:,.2f}.")
                break
    elif fltGoal <= intDeposit:
        print("No goal amount specified or goal amount is less than or equal to current balance. Skipping goal prediction.")
        return
#Main Function for Input Gathering and Validation
def main():
    # Input Validation for Original Deposit
    while True:
        try:
            intOriginalDeposit = input("What is the Original Deposit (Positive Value): ")
            intOriginalDeposit = int(intOriginalDeposit)
            if intOriginalDeposit <= 0:
                print("Input must be a positive numeric value")
            else:
                break
        except ValueError:
            print("Input must be a positive numeric value")
    # Input Validation for Interest Rate
    while True:
        try:
            intInterestRate = input("What is the Interest Rate (Positive Value): ")
            intInterestRate = float(intInterestRate)
            if intInterestRate <= 0:
                print("Input must be a positive numeric value")
            else:
                fltMonthlyInterestRate = intInterestRate/12
                break
        except ValueError:
            print("Input must be a positive numeric value")
    # Input Validation for Number of Months
    while True:
        try:
            intMonths = input("What is the Number of Months (Positive Value): ")
            intMonths = int(intMonths)
            if intMonths <= 0:
                print("Input must be a positive numeric value")
            else:
                break
        except ValueError:
            print("Input must be a positive numeric value")
    # Input Validation for Goal Amount
    while True:
        try:
            intGoalAmount = input("What is the Goal Amount (can enter 0 but not negative): ")
            intGoalAmount = float(intGoalAmount)
            if intGoalAmount < 0:
                print("Input must be 0 or greater")
            else:
                break
        except ValueError:
            print("Input must be 0 or greater")
    # Call the compound interest function
    print(f"{intOriginalDeposit, intInterestRate, fltMonthlyInterestRate, intMonths, intGoalAmount}")
    compound_interest(intOriginalDeposit, fltMonthlyInterestRate, intMonths, intGoalAmount)
main()