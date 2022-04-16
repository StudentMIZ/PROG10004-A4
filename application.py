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


def countdown(end):                                                                                                     # defines and declares function 'countdown', which is used to create a list of integer values up to the number the user inputted when asked
    i = 1                                                                                                               # sets the counter to 1, don't want to include 0 in the list as there is no 'Sensor 0'
    slist = []                                                                                                          # creates an empty list, 'slist', in which values will later be added
    while i <= end:                                                                                                     # this makes the function loop to this point until the last integer value in the list is equal to the number that was inputted
        slist.append(i)                                                                                                 # adds the integer values to the empty list
        i +=1                                                                                                           # increments the counter 'i' by 1 for every loop, until i is <= to the integer the user inputted
    return(slist)


class Application:
    sensorDict = {}
    def __init__(self):                                                                                                 #class constructor with all needed attributes
        self._listSensors = [list]
        self._Neighbours = "A"
        self._id = []
        self._numNeighbours = [list]
        
        
    def createSensors(self):                                                                                            #method that asks the user to input information for each sensor, including the neighbours, distance, oxygen, and temperature   
        while True:
            try:
                numCheck = int(input("Enter the number of sensors: "))                                                  #asks user to input number of sensors
                if(numCheck < 1):                                                                                       #if statement to make sure a valid amount is inputted, and if not it is shown as an error, and continues
                    print("This is an invalid entry for the number of sensors!", "\n")                                  #informs the user of an invalid entry
                    continue
            except ValueError:                                                                                          #if not a numeric input, will give an error and go back
                print("This is an invalid entry for the number of sensors!", "\n")                                      #informs the user of an invalid entry
                continue
            
            else:                                                                                                       #if not an error, it will run the following commands
                self._listSensors = countdown(numCheck)                                                                 #makes a list of sensors, using the countdown method and based on the user's input
                print(self._listSensors)
                for _ in range(len(self._listSensors)):                                                                 #will repeat the following commands for each value in the sensor list
                    while True: 
                        alphaCheck = input("Enter the Sensor Id: ")                                                     #asks user to input the sensor Id for the given sensor
                        if alphaCheck.isalpha():
                            self._id.extend(alphaCheck)
                            print(self._id)
                            for _ in alphaCheck:                                                                        #once user has inputted a valid id, it runs the next commands
                                while True:                                                                             #while loop is used to look out for errors on user's part
                                    try:
                                        alphaCheck2 = int(input("Enter the number of neighbours: "))                    #asks the user for the number of neighbours for each sensor
                                        if(alphaCheck2 < 0):                                                            #makes sure that the input can't be lower than 0, as it doesn't make sense
                                            print("This is an invalid entry for the number of neighbours!", "\n")
                                            continue
                                    except ValueError:                                                                  #makes sure the correct type of value is inputted by the user
                                        print("This is an invalid entry for the number of neighbours!", "\n")
                                        continue
            
                                    else:
                                        self._numNeighbours = countdown(alphaCheck2)                                    #will create a list of the given sensor's neighbours so that the following command will run for each value in that list
                                        print(self._numNeighbours)
                                        for _ in range(len(self._numNeighbours)):                                       #will run based on the value in the list made earlier
                                            while True:
                                                alphaCheck3 = input("Enter the neighbor for the sensor: ")              #asks the user to input the neighbour for the given sensor
                                                if alphaCheck3.isalpha():                                               #will make sure the user inputted a letter or a string of letters
                                                    self._Neighbours = alphaCheck3
                                                    for _ in self._Neighbours:                                          #will run for each neighbour for the given sensor
                                                        while True:
                                                            try:
                                                                numCheck2 = int(input("Enter the distance to the neighbour: "))                                 #asks the user to input the distance to the given neighbour
                                                                if(numCheck2 < 0):                                                                              #makes sure that the input is valid, above 0
                                                                    print("This is an invalid entry for the neighbour's name and/or distance!", "\n")           #informs the user of an invalid entry
                                                                    continue
                                                            except ValueError:                                                                                  #makes sure that the type of the value inputted is valid
                                                                print("This is an invalid entry for the neighbour's name and/or distance!", "\n")               #informs the user of an invalid entry
                                                                continue
                                                        
                                                            else:                                                                                               #stops the loop once the conditions are met
                                                                break
                                            
                                                    break                                                                                                       #breaks the loop once the conditions are met
                                                else:
                                                    print("This is an invalid entry for the neighbour's name and/or distance!", "\n")                           #informs the user of an invalid entry(neighbour name)
                                                    continue
                                    break
                                for _ in alphaCheck:                                                                        #for loop for every value in alphaCheck list, which holds sensor id list
                                    while True:
                                        try:
                                            numCheck3 = int(input("Enter the Oxygen level in %: "))                         #asks the user to input the O2 level for the given sensor
                                            if(numCheck3 < 0 or numCheck3 > 100):                                           #if condition to make sure input is valid (range between 0 and 100)
                                                print("This is an invalid entry for the oxygen level!", "\n")               #informs the user of an invalid entry
                                                continue
                                        except ValueError:                                                                  #makes sure that the correct type of value is inputted
                                            print("This is an invalid entry for the oxygen level!", "\n")                   #informs the user of an invalid entry
                                            continue
                                                        
                                        else:
                                            for _ in alphaCheck:                                                            #for loop runs for every item in the alphaCheck list, after the earlier for loop
                                                while True:
                                                    try:
                                                        numCheck4 = int(input("Enter the temperature measurement(°C): "))   #asks the user to input the temperature readings from the sensor
                                                        if(numCheck4 < -88 or numCheck4 > 58):                              #if loop condition used to make sure valid temperature readings are inputted(lowest and highest reading found on Earth)        
                                                            print("This is an invalid entry for the temperature!")          #informs the user of an invalid entry
                                                            continue
                                                    except ValueError:                                                      #makes sure that the correct type of value is inputted
                                                        print("This is an invalid entry for the temperature!")              #informs the user of an invalid entry
                                                        continue
                                                    else:
                                                        break                                                               #loop is broken once conditions are met, for every sensor
                                                    
                                            break                                                                           #break is used to make sure that the loop isn't infinite, asking for temperature and O2 readings
                            break                                                                                           #break is used to make sure that the loop isn't infinite, asking for number of neighbours and such
                        else:
                            print("This is an invalid entry for sensor Id!", "\n")                                          #informs the user of an invalid entry
                            continue                                                                                        #goes back in the loop to ask for a correct value for the sensor id
                break                                                                                                       #break is used to make sure that the loop isn't infinite, asking for sensor id and the following questions
                    

    
    def findPath(self, start, end, graph):                                                            
        route = []                                                                              
        queue = [[start]]                                                                       #this is the queue to go over the dictionary
        if start == end:                                                                        #condition runs if the source and destination sensor are the same
            print("This is the same sensor")                                                    #returns a message saying that the source and destination sensor inputted by the user is the same
            return
        else:                                                                                   #runs as long as the source and destination sensor are not the same
            while queue:                                                                        #while loop usd to go over the given graph
                path = queue.pop(0)                                                             #creates the path variable which is a list and removes the 0 index
                sensor = path[-1]
                if sensor not in route:                                                         #checks if the sensor in the dictionary is not gone over
                    neighbours = graph[sensor]
                    for _ in neighbours:                                                        #for loop that goes over all the neighbours for the sensor
                        new_path = list(path)                                                   #creats a variable that acts as a list for the 'newpath'
                        new_path.append(_)                                                      #appends the sensors to the destination into the list
                        queue.append(new_path)
                        if _ == end:                                                            #if condition runs when the destination sensor is reached
                            print("Path = ", *new_path)                                         #prints out the path taken from the source sensor to the destination sensor
                            return
                    
                    route.append(sensor)                                                        #appens the value sensor to the route list, so the path will be saved
 
                else:
                    print("A path between the two sensor doesn't exist!")                       #returns a message telling the user that a path between the two sensors doesn't exist
                    return
        
    def convertToDictionary(self):
        sensorDict = {}                                                                                         #sensorDict that is an empty list, that will be filled with values later
        for _ in self._id:                                                                                      #for loop to go over each sensor id inputted by the user during the createSensors function
            sensorDict[_] = []                                                                                  #for everything in the selfid list, a key is made using the values
        print(sensorDict)
        for key in sensorDict:                                                                                  #for loop to go over each key now in the sensorDict
            while True:                                                                                         #while loop to repeat the nested loop as long as the condition remains True, helps with exception handling
                try:
                    print("\n", "Sensor", key)
                    numNeighbours = int(input("Enter the number of neighbours: "))                              #asks the user to input the number of neighbours for the given id
                    if(numNeighbours < 0):                                                                      #if loop used to make sure a valid entry is made
                        print("This is an invalid entry for the number of neighbours!")                         #informs the user of an invalid entry
                        continue
                except ValueError:                                                                              #used to make sure only int values are inputted
                    print("This is an invalid entry for the number of neighbours!")                             #informs the user of an invalid entry
                    continue
                else:
                    neighbourlist = countdown(numNeighbours)                                                    #runs the countdown method, making a list based on the user's input
                    for _ in neighbourlist:                                                                     #for loop used for every index in the created list
                        while True:
                            try:
                                sensorDict[key] += (input("Enter the neighbour: ")), (int(input("Enter the distance to the neighbour: ")))      #asks the user for the neighbour and the distance to the neighbours
                            except ValueError:                                                                                                  #makes sure only the correct type of value is inputted
                                print("This is an invalid entry!")
                                continue
                            else:
                                print(sensorDict)
                                break                                                                           #breaks the for loop once all values are inputted, bringing it back to the next sensor ID 
                    break
        print(sensorDict)
        if __name__ == "__main__":
            graph = sensorDict                                                                                  #graph variable is equal to the earlier made sensorDict dictionary
        self.findPath(input("Enter the source sensor: "), input("Enter the destination sensor: "), graph)       #asks the user to input the source and destination sensor
        
        

        
         
obj1 = Application()
obj1.createSensors()
obj1.convertToDictionary()



#base case when start is equal to end, maximum distance, chosen node; newpath = findPath(graph, chosenNode, end, path)