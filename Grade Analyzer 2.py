#Grade Analyzer
##Import Libraries
import sys
import math
##Averaging Function
def averaging(sName, iGradesAmount, iGrade1, iGrade2, iGrade3, iGrade4, iLowestGrade):
    iAverage = (iGrade1 + iGrade2 + iGrade3 + iGrade4 - iLowestGrade) / (iGradesAmount)
    print(f"{sName} average grade is: {iAverage:.2f}" )
    gradingScale(iAverage)
#Grade Scale Function
def gradingScale(iAverage):
    if iAverage >= 97.0:
        letterGrade = "A+"
    elif 96.9 >= iAverage:
        letterGrade = "A"
    elif 93.9 >= iAverage:
        letterGrade = "A-"
    elif 89.9 >= iAverage:
        letterGrade = "B+"
    elif 86.9 >= iAverage:
        letterGrade = "B"
    elif 83.9 >= iAverage:
        letterGrade = "B-"
    elif 79.9 >= iAverage:
        letterGrade = "C+"
    elif 76.9 >= iAverage:
        letterGrade = "C"
    elif 73.9 >= iAverage:
        letterGrade = "C-"
    elif 69.9 >= iAverage:
        letterGrade = "D+"
    elif 66.9 >= iAverage:
        letterGrade = "D"
    elif 63.9 >= iAverage:
        letterGrade = "D-"
    else:
        letterGrade = "F"
    print(f"Letter grade for the test is {letterGrade}")
#Drop Lowest Function
def dropLowest(sName, iGrade1, iGrade2, iGrade3, iGrade4):
    iLowestGrade = iGrade1
    if iGrade1 < iLowestGrade:
        iLowestGrade = iGrade1
    if iGrade2 < iLowestGrade:
        iLowestGrade = iGrade2
    if iGrade3 < iLowestGrade:
        iLowestGrade = iGrade3
    if iGrade4 < iLowestGrade:
        iLowestGrade = iGrade4
    averaging(sName, 3, iGrade1, iGrade2, iGrade3, iGrade4, iLowestGrade)
##Main Program 
def main():
    sUserNameInput = input("Enter the name of the person we are calculating grades for: ")
    iGrade1 = int(input("Enter the first grade: "))
    iGrade2 = int(input("Enter the second grade: "))
    iGrade3 = int(input("Enter the third grade: "))
    iGrade4 = int(input("Enter the fourth grade: "))
    if iGrade1 < 0 or iGrade2 < 0 or iGrade3 < 0 or iGrade4 < 0:
        print("Invalid Input. Grades cannot be negative.")
        sys.exit()
    sGradeDrop = str(input("Would you like to drop the lowest grade before averaging? (Y/N): ")).upper()
    if sGradeDrop == "Y":
        dropLowest(sUserNameInput, iGrade1, iGrade2, iGrade3, iGrade4)
    elif sGradeDrop == "N":
        averaging(sUserNameInput, 4, iGrade1, iGrade2, iGrade3, iGrade4, 0)
    else:
        print("Invalid Input. Please enter Y or N.")
        sys.exit()
##Execution
main()