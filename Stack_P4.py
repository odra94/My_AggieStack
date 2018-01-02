# Oscar Reyes
# CSCE 489 - Cloud Computing
# Project 4

from Classes import *;
import Helpers;

# Variables to store text file configurations in an array line by line
# Each line in the array is a line in the text file
hdwrConfig = []
imageConfig = []
flavorConfig = []

# Arrays contain an array of objects for each respective racks, images and flavors available
racks = []
images = []
flavors = []
vServersNotEvac = []


# Variables to check if configuration has been uploaded
uploadedHdwrConfig = False
uploadedImageConfig = False
uploadedFlavorConfig = False


#Start of program

cont = True
logFile = open("log.txt", "a")
while cont:
    commandInput = input(">> ")
    if commandInput == "exit":
        cont = False
        logFile.writelines("[SUCCESS] " + commandInput + "\n")
        break
    line = commandInput.split()

    try:

        if line[0] == "aggiestack":
            if line[1] == "config":
                if line[2] == "--hardware":
                    extension = line[3][-4:]
                    if extension == ".txt":
                        try:
                            logFile.writelines("[SUCCESS] " + commandInput + "\n") # Writing to log file
                            hdwrFile = open(line[3], "r")
                            array = []

                            #Put the lines of the file into an array
                            for line in hdwrFile:
                                array.append(line.replace("\n",""))

                            hdwrConfig = array

                            # for line in hdwrConfig:
                            #     print(line)

                            #Create array of racks
                            racks = Helpers.createRacks(hdwrConfig)

                            hdwrFile.close()
                            print("Hardware configuration has been saved and racks have been created.")
                            uploadedHdwrConfig = True
                        except FileNotFoundError:
                            print("Command was executed. However, file specified not found.")

                    else:
                        # Error in fourth argument
                        print("Fourth argument in the input not accepted.")
                        print("Make sure your file name includes the \'.txt\' extension. Please try again.")
                        logFile.write("[FAILURE] " + commandInput + "\n")
                elif line[2] == "--images":
                    extension = line[3][-4:]
                    if extension == ".txt":
                        try:
                            logFile.write("[SUCCESS] " + commandInput + "\n")
                            imgFile = open(line[3], "r")
                            array = []

                            #Put the lines of the image file into an array
                            for line in imgFile:
                                array.append(line)

                            imageConfig = array

                            # Create array of images
                            images = Helpers.createImage(imageConfig)

                            imgFile.close()
                            print("Image configuration has been saved.")
                            uploadedImageConfig = True
                        except FileNotFoundError:
                            print("Command was executed. However, file specified not found.")


                    else:
                        # Error in fourth argument
                        print("Fourth argument in the input not accepted.")
                        print("Make sure your file name includes the \'.txt\' extension. Please try again.")
                        logFile.write("[FAILURE] " + commandInput + "\n")
                elif line[2] == "--flavors":
                    extension = line[3][-4:]
                    if extension == ".txt":
                        try:
                            logFile.write("[SUCCESS] " + commandInput + "\n")
                            flavorFile = open(line[3], "r")
                            array = []

                            # Put lines of the flavors file into an array
                            for line in flavorFile:
                                array.append(line)

                            flavorConfig = array

                            # Create array of flavors
                            flavors = Helpers.createFlavors(flavorConfig)

                            flavorFile.close()
                            print("Flavor configuration has been saved.")
                            uploadedFlavorConfig = True
                        except FileNotFoundError:
                            print("Command was executed. However, file specified not found.")

                    else:
                        # Error in fourth argument
                        print("Fourth argument in the input not accepted.")
                        print("Make sure your file name includes the \'.txt\' extension. Please try again.")
                        logFile.write("[FAILURE] " + commandInput + "\n")
                else:
                    print("Third argument in the input not accepted. Please try again.")
                    logFile.write("[FAILURE] " + commandInput + "\n")
            elif line[1] == "show":
                #another if for hardware and images goes here
                if line[2] == "hardware":
                    if uploadedHdwrConfig:
                        logFile.write("[SUCCESS] " + commandInput + "\n")
                        Helpers.showHardwareInfo(racks)

                    else:
                        logFile.write("[FAILURE] " + commandInput + "\n")
                        print("Hardware information has not been uploaded yet. Please upload hardware configuration file.")

                elif line[2] == "images":
                    if uploadedImageConfig:
                        logFile.write("[SUCCESS] " + commandInput + "\n")
                        Helpers.showImageInfo()

                    else:
                        logFile.write("[FAILURE] " + commandInput + "\n")
                        print("Image information has not been uploaded yet. Please upload image configuration file.")

                elif line[2] == "flavors":
                    if uploadedFlavorConfig:
                        logFile.write("[SUCCESS] " + commandInput + "\n")
                        Helpers.showFlavorInfo(flavors)

                    else:
                        logFile.write("[FAILURE] " + commandInput + "\n")
                        print("Flavors information has not been uploaded yet. Please upload hardware configuration file.")

                elif line[2] == "all":
                    if uploadedHdwrConfig & uploadedImageConfig & uploadedFlavorConfig:
                        logFile.write("[SUCCESS] " + commandInput + "\n")
                        Helpers.showAllInfo(racks, images, flavors)


                    elif (not uploadedHdwrConfig) & uploadedImageConfig & uploadedFlavorConfig:
                        logFile.write("[FAILURE] " + commandInput + "\n")
                        print("Hardware information has not been uploaded yet. Please upload hardware configuration file.")

                    elif (not uploadedFlavorConfig) & uploadedImageConfig & uploadedHdwrConfig:
                        logFile.write("[FAILURE] " + commandInput + "\n")
                        print("Flavor information has not been uploaded yet. Please upload hardware configuration file.")

                    elif (not uploadedImageConfig) & uploadedHdwrConfig & uploadedFlavorConfig:
                        logFile.write("[FAILURE] " + commandInput + "\n")
                        print("Image information has not been uploaded yet. Please upload hardware configuration file.")

                    else:
                        logFile.write("[FAILURE] " + commandInput + "\n")
                        print("No configuration has not been uploaded yet. Please upload all needed configurations.")

                else:
                    #Error for the third argument goes here
                    print("Third argument in the input not accepted. Please try again.")
                    logFile.write("[FAILURE] " + commandInput + "\n")

            elif line[1] == "admin":

                if line[2] == "show":

                    if line[3] == "hardware":
                        logFile.write("[SUCCESS] " + commandInput + "\n")
                        Helpers.adminShowHardware(racks)

                    elif line[3] == "instances":
                        logFile.write("[SUCCESS] " + commandInput + "\n")
                        Helpers.adminShowInstances(racks)

                    else:
                        print("Fourth argument in the input is not accepted. Please try again.")
                        logFile.writelines("[FAILURE] " + commandInput + "\n")

                elif line[2] == "evacuate":
                    logFile.write("[SUCCESS] " + commandInput + "\n")
                    rackName = line[3]
                    vServersNotEvac = Helpers.adminEvacuateRack(rackName, racks)

                elif line[2] == "remove":
                    machineName = line[3]
                    logFile.write("[SUCCESS] " + commandInput + "\n")
                    Helpers.adminRemoveServer(machineName, racks)

                elif line[2] == "add":
                    newServer = Server()
                    if line[3] == "--mem":
                        newServer.mem = line[4]
                        if line[5] == "--disk":
                            newServer.numDisks = line[6]
                            if line[7] == "--vcpus":
                                newServer.numCores = line[8]
                                if line[9] == "--ip":
                                    newServer.ip = line[10]
                                    if line[11] == "--rack":
                                        newServer.rackName = line[12]
                                        if line[13]:
                                            newServer.machineName = line[13]
                                            Helpers.adminAddServer(newServer, racks)

                                        else:
                                            print("13th argument in the input is not accepted or is empty. Please try again.")
                                            logFile.writelines("[FAILURE] " + commandInput + "\n")
                                    else:
                                        print("12th argument in the input is not accepted. Please try again.")
                                        logFile.writelines("[FAILURE] " + commandInput + "\n")
                                else:
                                    print("10th argument in the input is not accepted. Please try again.")
                                    logFile.writelines("[FAILURE] " + commandInput + "\n")
                            else:
                                print("8th argument in the input is not accepted. Please try again.")
                                logFile.writelines("[FAILURE] " + commandInput + "\n")
                        else:
                            print("6th argument in the input is not accepted. Please try again.")
                            logFile.writelines("[FAILURE] " + commandInput + "\n")

                    else:
                        print("Fourth argument in the input is not accepted. Please try again.")
                        logFile.writelines("[FAILURE] " + commandInput + "\n")


                elif line[2] == "can_host":

                    error = Helpers.canHost(line[3], line[4], racks, flavors)

                    if error == 3:
                        print("Third argument in the input is not accepted. Please try again.")
                        logFile.writelines("[FAILURE] " + commandInput + "\n")
                    elif error == 4:
                        print("Fourth argument in the input is not accepted. Please try again.")
                        logFile.writelines("[FAILURE] " + commandInput + "\n")

                    else:
                        logFile.write("[SUCCESS] " + commandInput + "\n")

                else:
                    #Error for the third argument goes here
                    print("Third argument in the input is not accepted. Please try again.")
                    logFile.writelines("[FAILURE] " + commandInput + "\n")
            elif line[1] == "server":

                if line[2] == "create":
                    if line[3] == "--image":
                        imageToBootFrom = line[4]
                        if line[5] == "--flavor":
                            flavorName = line[6]
                            virtualServerName = line[7]
                            Helpers.createInstance(imageToBootFrom, flavorName, virtualServerName, racks, images, flavors)

                        else:
                            print("Sixth argument in the input not accepted. Please try again.")
                            logFile.writelines("[FAILURE] " + commandInput + "\n")

                    else:
                        print("Fourth argument in the input not accepted. Please try again.")
                        logFile.writelines("[FAILURE] " + commandInput + "\n")
                elif line[2] == "delete":

                    instanceName = line[3]

                    print("Instance name: " + instanceName)

                    Helpers.deleteInstance(instanceName, racks)

                elif line[2] == "list":
                    Helpers.adminServerList(racks)

                else:
                    # Error message for the fourth argument
                    print("Third argument in the input not accepted. Please try again.")
                    logFile.writelines("[FAILURE] " + commandInput + "\n")

            else:
                #Error message for the second argument goes here
                print("Second argument in the input not accepted. Please try again.")
                logFile.writelines("[FAILURE] " + commandInput + "\n")
        else:
            #Error message for the first argument goes here
            print("First argument in the input is not accepted. Please try again.")
            logFile.writelines("[FAILURE] " + commandInput + "\n")
    except IndexError:
        print("Not enough arguments for command you entered.")

logFile.close()

