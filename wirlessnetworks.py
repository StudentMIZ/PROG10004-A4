
class WirelessNetworks:
    ADHOC_Mode = "ON"
    BRAND_NAME = "Cisco"

    def greetMessage(self):
        print("******************************************************************************", "\n", "Welcome to the company's IoT-Based Health System.", "\n", "These are sensors of", WirelessNetworks.BRAND_NAME, "brand, and their Ad Hoc Mode is", WirelessNetworks.ADHOC_Mode, "\n" "****************************************************************************** ")

    def __init__(self):
        self._id = "a"
        self._oxygenLevel = 0
        self._temperature = 0

    def setId(self):
        while True:
            alphaCheck = input("Enter the Sensor Id: ")
            if alphaCheck.isalpha():
                self._id = alphaCheck
                break
            
            else:
                print("This is an invalid entry for sensor Id!", "\n")
                
    def setOxygen(self):
        while True:
            alphaCheck2 = input("Enter the Oxygen level in %: ")
            if alphaCheck2.isnumeric():
                self._oxygenLevel = alphaCheck2
                break
            
            else:
                print("This is an invalid entry for the oxygen level!", "\n")
                

    def setTemperature(self):
        while True:
            alphaCheck3 = input("Enter the termperature measurement: ")
            if alphaCheck3.isnumeric():
                self._temperature = alphaCheck3
                break
            
            else:
                print("This is an invalid entry for the temperature!", "\n")
                




obj = WirelessNetworks()

obj.greetMessage()
obj.setId()
obj.setOxygen()
obj.setTemperature()