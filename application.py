
def countdown(end):                                                     # defines and declares function 'countdown', which is used to create a list of integer values up to the number the user inputted when asked
    i = 1                                                               # sets the counter to 1, don't want to include 0 in the list as there is no 'Sensor 0'
    slist = []                                                          # creates an empty list, 'slist', in which values will later be added
    while i <= end:                                                     # this makes the function loop to this point until the last integer value in the list is equal to the number that was inputted
        slist.append(i)                                                 # adds the integer values to the empty list
        i +=1                                                           # increments the counter 'i' by 1 for every loop, until i is <= to the integer the user inputted
    return(slist)
class Application:
    
    def __init__(self):
        self._listSensors = [list]
        self._Neighbours = "A"
        self._id = "A"
        self._numNeighbours = [list]
        
        
    def createSensors(self):
        while True:
            try:
                numCheck = int(input("Enter the number of sensors: "))
                if(numCheck < 1):
                    print("This is an invalid entry for the number of sensors!", "\n")
                    continue
            except ValueError:
                print("This is an invalid entry for the number of sensors!", "\n")
                continue
            
            else:
                self._listSensors = countdown(numCheck)
                print(self._listSensors)
                for _ in range(len(self._listSensors)):
                        alphaCheck = input("Enter the Sensor Id: ")
                        if alphaCheck.isalpha():
                            self._id = alphaCheck
                            for _ in self._id:
                                while True:
                                    try:
                                        alphaCheck2 = int(input("Enter the number of neighbours: "))
                                        if(alphaCheck2 < 0):
                                            print("This is an invalid entry for the number of neighbours!", "\n")
                                            continue
                                    except ValueError:
                                        print("This is an invalid entry for the number of neighbours!", "\n")
                                        continue
            
                                    else:
                                        self._numNeighbours = countdown(alphaCheck2)
                                        print(self._numNeighbours)
                                        for _ in range(len(self._numNeighbours)):
                                            alphaCheck3 = input("Enter the neighbor for the sensor: ")
                                            if alphaCheck3.isalpha():
                                                self._Neighbours = alphaCheck3
                                                for _ in self._Neighbours:
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
                                                break
                                    break
                        else:
                            print("This is an invalid entry for sensor Id!", "\n")
                            break
                break
                    

                
    
    def convertToDictionary(self):
        pass
    
    def findPath(self):
        pass
    
obj1 = Application()
obj1.createSensors()