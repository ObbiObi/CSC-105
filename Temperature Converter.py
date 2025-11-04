irunTime = 1
print("Anthony Brown's Temperature Converter:")
##TemperatureCoversionFunction
def temperatureConversion(iTemperature, sScaleType):
    if sScaleType == "F":
        iCelsius = round(((iTemperature - 32) * 5.0/9.0), 1)
        print(f"The Temperature in Celcius is: {iCelsius} C")
    elif sScaleType == "C":
        iFahrenheit = round(((iTemperature * 9.0/5.0) + 32), 1)
        print(f"The Temperature in Fahrenheit is: {iFahrenheit} F")
##Main Program
def mainProgram():
    global irunTime
    while irunTime == 1:
        #Option Selection to leave code
        print("""Please Select a Option:
        1. Temp Converter
        2. Exit""")
        sOption = input("Option: ")
        ##Inputs
        if sOption == "1":
            #TemperatureType Input
            while True:
               print("What Temperature are you Using F(Fahrenheit) or C(Celcius)")
               sType = str(input("Please Enter F or C: ")).upper()
               if sType == "F" or sType == "C":
                   break
               else:
                   print("Invalid Answer.")
            #TemperatureValue Input
            while True:
                print("What is the Tempearture?")
                iTemp = int(input("Please Enter the Temperature: "))
                if iTemp > 212 and sType == "F":
                    print("Invalid Number. Cant be Greater than 212")
                elif iTemp > 100 and sType == "C":
                    print("Invalid Number. Cant be Greater than 100")
                else:
                    break
            #Function Call(Temperature Conversion)
            temperatureConversion(iTemp, sType)
        elif sOption == "2":
            print("Exiting")
            return irunTime == 0
        else:
            print("Invalid Option. Enter again")
mainProgram()