'''Code written by Muhammad Zurayn Imtiaz
PROG10004 Class 1221_78492
April 16, 2022'''

'''Write an OO program that greets the user with a welcoming message and prints the ad hoc mode 
and the sensors brand. Afterwards, the application will ask for the following components of the 
wireless ad hoc sensor network: 1) the total number of deployed sensors, 2) the sensor 
Identification (Id) for each sensor, 3) the number of neighbouring sensors for each sensor, 4) the
geographic distance(s) between a sensor and its neighbouring sensor(s), 5) the oxygen 
percentage level saturated in the blood cells (SpO2), and 6) the temperature measurement for 
each sensor. Afterwards, the application will ask the users to enter the source sensor Id and 
destination sensor Id to route a message and will print the traversed path and the entire graph.'''


class WirelessNetworks:
    ADHOC_Mode = "ON"                                                           #value is immutable, a class variable
    BRAND_NAME = "Cisco"                                                        #value is immutable, a class variable

    def greetMessage(self):                                                     #class method that prints a greeting message for the user
        print("******************************************************************************", "\n", "Welcome to the company's IoT-Based Health System.", "\n", "These are sensors of", WirelessNetworks.BRAND_NAME, "brand, and their Ad Hoc Mode is", WirelessNetworks.ADHOC_Mode, "\n" "****************************************************************************** ")

    def __init__(self):
        self._id = "a"
        self._oxygenLevel = 0
        self._temperature = 0

    def setId(self):                                                            #mutator method made to be more user friendly
        while True:
            alphaCheck = input("Enter the Sensor Id: ")                         #asks the user for the sensor id
            if alphaCheck.isalpha():                                            #if condition used to make sure the input is of the alphabet
                self._id = alphaCheck
                break
            
            else:
                print("This is an invalid entry for sensor Id!", "\n")          #informs the user of an invalid entry
                
    def setOxygen(self):                                                        #mutator method made to be more user friendly
        while True:
            alphaCheck2 = input("Enter the Oxygen level in %: ")                #asks the user to input the O2 levels
            if alphaCheck2.isnumeric():                                         #if condition used to make sure that the input is valid
                self._oxygenLevel = alphaCheck2
                break
            
            else:
                print("This is an invalid entry for the oxygen level!", "\n")   #informs the user of an invalid entry
                

    def setTemperature(self):                                                   #mutator method made to be more user friendly
        while True:
            alphaCheck3 = input("Enter the termperature measurement(°C): ")     #asks the user to input the temperature measurement
            if alphaCheck3.isnumeric():                                         #if condition used to make sure that the input is valid(numeric)
                self._temperature = alphaCheck3
                break
            
            else:
                print("This is an invalid entry for the temperature!", "\n")    #informs the user of an invalid entry