
class WirelessNetworks:
    ADHOC_Mode = "ON"
    BRAND_NAME = "Cisco"

    def greetMessage(self):
        print("******************************************************************************", "\n", "Welcome to the company's IoT-Based Health System.", "\n", "These are sensors of", WirelessNetworks.BRAND_NAME, "brand, and their Ad Hoc Mode is", WirelessNetworks.ADHOC_Mode, "\n" "****************************************************************************** ")

    def __init__(self):
        self._id = "a"
        self._oxygenLevel = 0
        self._temperature = 0

    def setid(self):
        while True:
            alphaCheck = input("Enter the Sensor Id: ")
            if alphaCheck.isalpha():
                self._id = alphaCheck
                break
            
            else:
                print("This is an invalid entry for sensor Id!")
                




obj = WirelessNetworks()

obj.greetMessage()
obj.setid()