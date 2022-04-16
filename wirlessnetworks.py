
class WirelessNetworks:
    ADHOC_Mode = "ON"
    BRAND_NAME = "Cisco"

    def greetMessage(self):
        print("******************************************************************************", "\n", "Welcome to the company's IoT-Based Health System.", "\n", "These are sensors of", WirelessNetworks.BRAND_NAME, "brand, and their Ad Hoc Mode is", WirelessNetworks.ADHOC_Mode, "\n" "****************************************************************************** ")

    def __init__(self):
        self._id = "a"
        self._oxygenLevel = 0
        self._temperature = 0



obj = WirelessNetworks()
obj.greetMessage()
