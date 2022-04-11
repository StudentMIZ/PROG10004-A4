
from collections import defaultdict

def countdown(end):                                                                                                 # defines and declares function 'countdown', which is used to create a list of integer values up to the number the user inputted when asked
    i = 1                                                                                                           # sets the counter to 1, don't want to include 0 in the list as there is no 'Sensor 0'
    slist = []                                                                                                      # creates an empty list, 'slist', in which values will later be added
    while i <= end:                                                                                                 # this makes the function loop to this point until the last integer value in the list is equal to the number that was inputted
        slist.append(i)                                                                                             # adds the integer values to the empty list
        i +=1                                                                                                       # increments the counter 'i' by 1 for every loop, until i is <= to the integer the user inputted
    return(slist)


class Application:
    
    def __init__(self):                                                                                             #class constructor with all needed attributes
        self._listSensors = [list]
        self._Neighbours = "A"
        self._id = "A"
        self._numNeighbours = [list]
        
        
    def createSensors(self):                                                                                        #method that asks the user to input information for each sensor, including the neighbours, distance, oxygen, and temperature   
        while True:
            try:
                numCheck = int(input("Enter the number of sensors: "))                                              #asks user to input number of sensors
                if(numCheck < 1):                                                                                   #if statement to make sure a valid amount is inputted, and if not it is shown as an error, and continues
                    print("This is an invalid entry for the number of sensors!", "\n")
                    continue
            except ValueError:                                                                                      #if not a numeric input, will give an error and go back
                print("This is an invalid entry for the number of sensors!", "\n")
                continue
            
            else:                                                                                                   #if not an error, it will run the following commands
                self._listSensors = countdown(numCheck)                                                             #makes a list of sensors, using the countdown method and based on the user's input
                print(self._listSensors)
                for _ in range(len(self._listSensors)):                                                             #will repeat the following commands for each value in the sensor list
                        alphaCheck = input("Enter the Sensor Id: ")                                                 #asks user to input the sensor Id for the given sensor
                        if alphaCheck.isalpha():
                            self._id = alphaCheck
                            for _ in self._id:                                                                      #once user has inputted a valid id, it runs the next commands
                                while True:                                                                         #while loop is used to look out for errors on user's part
                                    try:
                                        alphaCheck2 = int(input("Enter the number of neighbours: "))                #asks the user for the number of neighbours for each sensor
                                        if(alphaCheck2 < 0):                                                        #makes sure that the input can't be lower than 0, as it doesn't make sense
                                            print("This is an invalid entry for the number of neighbours!", "\n")
                                            continue
                                    except ValueError:                                                              #makes sure the correct type of value is inputted by the user
                                        print("This is an invalid entry for the number of neighbours!", "\n")
                                        continue
            
                                    else:
                                        self._numNeighbours = countdown(alphaCheck2)                                #will create a list of the given sensor's neighbours so that the following command will run for each value in that list
                                        print(self._numNeighbours)
                                        for _ in range(len(self._numNeighbours)):                                   #will run based on the value in the list made earlier
                                            alphaCheck3 = input("Enter the neighbor for the sensor: ")              #asks the user to input the neighbour for the given sensor
                                            if alphaCheck3.isalpha():                                               #will make sure the user inputted a letter or a string of letters
                                                self._Neighbours = alphaCheck3
                                                for _ in self._Neighbours:                                          #will run for each neighbour for the given sensor
                                                    while True:
                                                        try:
                                                            numCheck2 = int(input("Enter the distance to the neighbour: "))
                                                            if(numCheck2 < 0):
                                                                print("This is an invalid entry for the neighbour's name and/or distance!", "\n")
                                                                continue
                                                        except ValueError:
                                                            print("This is an invalid entry for the neighbour's name and/or distance!", "\n")
                                                            continue
                                                        
                                                        else:
                                                            break
                                            
                                            else:
                                                print("This is an invalid entry for the neighbour's name and/or distance!", "\n")
                                                continue
                                    break
                                for _ in self._id:
                                    while True:
                                        try:
                                            numCheck3 = int(input("Enter the Oxygen level in %: "))
                                            if(numCheck3 < 0):
                                                print("This is an invalid entry for the oxygen level!", "\n")
                                                continue
                                        except ValueError:
                                            print("This is an invalid entry for the oxygen level!", "\n")
                                            continue
                                                        
                                        else:
                                            for _ in self._id:
                                                while True:
                                                    try:
                                                        numCheck4 = int(input("Enter the temperature measurement: "))
                                                        if(numCheck4 < 0):
                                                            print("This is an invalid entry for the temperature!")
                                                            continue
                                                    except ValueError:
                                                        print("This is an invalid entry for the temperature!")
                                                        continue
                                                    else:
                                                        break
                                                    
                                            break
                        else:
                            print("This is an invalid entry for sensor Id!", "\n")
                            continue
                break
                    

                
    
    def convertToDictionary(self):
        sensorDict = {}
        for _ in self._listSensors:
            sensorDict[_] = None
        print(sensorDict)
        for key in sensorDict:
            sensorDict[key] = tuple(input("Enter the sensorId: "))
            numNeighbours = int(input("Enter the number of neighbours: "))
            neighbourlist = countdown(numNeighbours)
            for _ in neighbourlist:
                sensorDict[key] += (input("Enter the neighbour: "), int(input("Enter the distance to the neighbour: ")))
                print(sensorDict)
    
    def findPath(self):
        pass
    
obj1 = Application()
obj1.createSensors()
obj1.convertToDictionary()


