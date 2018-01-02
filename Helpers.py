# Helper functions for Stack_P4.py
from Classes import *;

def createRacks(hdwrConfig = []):

    numRacks = int(hdwrConfig[0])
    # print("Number of racks: " + str(numRacks))
    numMachines = int(hdwrConfig[numRacks+1])
    # print("Number of machines: " + str(numMachines))
    racks = []

    #Create the racks
    index = 1
    while index < numRacks+1:
        # print("Index: " + str(index))
        rack = Rack()
        # create rack and assign the storage capacity
        line = hdwrConfig[index].split()
        rack.rackName = line[0]
        rack.storageCap = int(line[1])

        # Add rack to racks array
        racks.append(rack)
        index += 1

    # print("Index after while loop: " + str(index))

    linesRemaining = numMachines + index + 1

    index += 1
    # print("Lines remaining: " + str(linesRemaining))
    #Assign the machines to each rack

    while index < linesRemaining:
        line = hdwrConfig[index].split()
        # print("Current line: " + hdwrConfig[index])
        server = Server()

        machineName = line[0]
        rackName = line[1]
        ip = line[2]
        mem = int(line[3])
        numDisks = int(line[4])
        numCores = int(line[5])

        server.__set__(machineName, rackName, ip, mem, numDisks, numCores)

        for rack in racks:
            if rack.rackName == server.rackName:
                rack.servers.append(server)
                rack.numMachines += 1

        index += 1

    return racks


def createFlavors(flavorConfig = []):

    numFlavors = int(flavorConfig[0])
    flavors = []

    #Create the flavors
    index = 1
    while index <= numFlavors:
        flavor = Flavor()
        # create rack and assign the storage capacity
        line = flavorConfig[index].split()
        flavor.size = line[0]
        flavor.mem = int(line[1])
        flavor.numDisks = int(line[2])
        flavor.numCores = int(line[3])

        # Add rack to racks array
        flavors.append(flavor)
        index += 1

    return flavors


def createImage(imageConfig = []):

    numImages = int(imageConfig[0])
    images = []

    #Create the images
    index = 1
    while index <= numImages:
        image = Image()
        # create rack and assign the storage capacity
        line = imageConfig[index].split()
        image.imageName = line[0]
        # print("Image name: " + image.imageName)
        image.imageSizeMB = int(line[1])
        # print("Image size in MB: " + str(image.imageSizeMB))
        image.imagePath = line[2]
        # print("Image path: " + image.imagePath)

        # Add rack to racks array
        images.append(image)
        index += 1

    return images


def showHardwareInfo(racks = []):

    print("Number of racks: " + str(len(racks)))
    for rack in racks:
        print("Rack name: " + rack.rackName)
        print("This rack has the following number of servers: " + str(len(rack.servers)))

        for server in rack.servers:

            print("Server name: " + server.rackName)
            print("Memory available: " + str(server.mem))
            print("Disks available: " + str(server.numDisks))
            print("Number of cores available: " + str(server.numCores))

        print()

def showImageInfo(images = []):

    print("Number of images: " + str(len(images)))
    for image in images:

        print("Image name: " + image.imageName)
        print("Image size in MB: " + str(image.imageSizeMB))
        print("Image path: " + image.imagePath)
        print()

def showFlavorInfo(flavors = []):

    print("Number of flavors: " + str(len(flavors)))
    for flavor in flavors:

        print("Flavor size: " + flavor.size)
        print("Memory in this flavor: " + str(flavor.mem))
        print("Number of disks: " + str(flavor.numDisks))
        print("Number of cores: " + str(flavor.numCores))
        print()


def showAllInfo(racks = [], images = [], flavors = []):
    showHardwareInfo(racks)
    print()
    showImageInfo(images)
    print()
    showFlavorInfo(flavors)


def adminShowHardware(racks = []):

    print("Number of racks: " + str(len(racks)))
    for rack in racks:
        print("Rack name: " + rack.rackName)
        print("This rack has the following number of servers: " + str(len(rack.servers)))

        for server in rack.servers:
            print("Server name: " + server.machineName)
            if not server.view:
                print("This server is currently not visible to data center. Only visible to admins")
            print("Memory available: " + str(server.unallocatedMem))
            print("Disks available: " + str(server.unallocatedDisks))
            print("Number of cores available: " + str(server.unallocatedCores))
        print()


def canHost(machineName, flavorSize, racks = [], flavors = []):

    error = 3

    machineFound = False
    enoughDisks = False
    enoughMem = False
    enoughCores = False

    potFlavorSize = Flavor()  # The size of flavor we are checking to host

    for flavor in flavors:
        if flavorSize == flavor.size:
            potFlavorSize = flavor.size

        else:
            print("Flavor specified not an option.")
            error = 4
            return error


    for rack in racks:
        for server in rack.servers:
            if server.view:
                if machineName == server.machineName:
                    machineFound = True
                    if server.unallocatedDisks > potFlavorSize.numDisks:
                        enoughDisks = True
                        if server.unallocatedMem > potFlavorSize.mem:
                            enoughMem = True
                            if server.unallocatedCores > potFlavorSize.numCores:
                                enoughCores = True



    if machineFound & enoughDisks & enoughMem & enoughCores:
        print("Yes.")
        error = 0
        return error

    else:
        print("Machine " + machineName + " is currently not able to host desired flavor type.")
        eroro = 0
        return error


# function to find a server to host instance
def findInstanceHost(desiredFlavor = Flavor(), racks = [] ):

    print("Looking for server to host your instance...")

    hostMachineName = ""
    enoughCores = False
    enoughDisks = False
    enoughMem = False


    for rack in racks:
        #TODO come check this again later
        for server in rack.servers:
            if server.view:

                print("Server unallocated Cores: " + str(server.unallocatedCores)  + " | Desired flavor Cores: " + str(desiredFlavor.numCores))
                print("Server unallocated Disks: " + str(server.unallocatedDisks) + " | Desired flavor Disks: " + str(desiredFlavor.numDisks))
                print("Server unallocated Mem: " + str(server.unallocatedMem) + " | Desired flavor Mem: " + str(desiredFlavor.mem))
                print()

                if server.unallocatedCores >= desiredFlavor.numCores:
                    enoughCores = True
                    if server.unallocatedDisks >= desiredFlavor.numDisks:
                        enoughDisks = True
                        if server.unallocatedMem >= desiredFlavor.mem:
                            enoughMem = True
                            hostMachineName = server.machineName
                            break

        if enoughCores & enoughDisks & enoughDisks:
            break

    if enoughCores & enoughDisks & enoughMem:
        print("Host machine has been found.")
        return hostMachineName
    else:
        print("Host not found.")


# function to create instance
def createInstance(imageToBootFrom, flavorSize, virtualServerName, racks = [], images = [], flavors = []):

    foundFlavor = False
    foundImage = False

    desiredFlavor = Flavor()
    desiredImage = Image()
    serverToHostOn = ""

    for flavor in flavors:
        if flavorSize == flavor.size:
            desiredFlavor = flavor
            foundFlavor = True

    for image in images:
        if imageToBootFrom == image.imageName:
            desiredImage = image
            foundImage = True

    serverToHostOn = findInstanceHost(desiredFlavor, racks)

    if foundImage & foundFlavor:
        for rack in racks:
            for server in rack.servers:
                if server.view:
                    if serverToHostOn == server.machineName:

                        vserver = virtualServer()
                        vserver.instanceName = virtualServerName
                        vserver.vServerDisks = desiredFlavor.numDisks
                        vserver.vServerMem = desiredFlavor.mem
                        vserver.image.__set__(desiredImage.imageName, desiredImage.imageSizeMB, desiredImage.imagePath)
                        vserver.flavor.__set__(desiredFlavor.size, desiredFlavor.mem, int(desiredFlavor.numDisks), int(desiredFlavor.numCores))

                        #Add instance and also update unallocated resources
                        server.virtualServers.append(vserver)
                        server.unallocatedMem -= vserver.vServerMem/1000 # convert to gigabytes
                        server.unallocatedDisks -= vserver.vServerDisks
                        server.unallocatedCores -= vserver.vServerCores

    else:
        print("Specified image or flavor not found. Please try again.")


# Delete instance name
def deleteInstance(instanceName, racks = []):

    instToRemove = virtualServer()
    rackName = ""
    serverName = ""
    for rack in racks:
        for server in rack.servers:
                for vServer in server.virtualServers:
                    if instanceName == vServer.instanceName:
                        instToRemove = vServer
                        rackName = rack.rackName
                        serverName = server.machineName


    try:
        for rack in racks:
            if rackName == rack.rackName:
                for server in rack.servers:
                    if serverName == server.machineName:
                        server.virtualServers.remove(instToRemove)
    except ValueError:
        print("Error. Value is not in the instances.")



# List all instances that are running
def adminServerList(racks = []):

    instancesExist = False
    print("Instances currently running: ")
    for rack in racks:
        if rack.servers:
            for server in rack.servers:
                if server.view:
                    if server.virtualServers:
                        instancesExist = True
                        for vServer in server.virtualServers:
                            print("Instance name: " + vServer.instanceName)
                            print("Image: " + vServer.image.imageName)
                            print("Flavor: " + vServer.flavor.size)
                            print()
        if not instancesExist:
            print("None.")


# Show on what physical server instances are running
def adminShowInstances(racks = []):

    instancesExist = False
    print("Instances currently running: ")
    for rack in racks:
        if rack.servers:
            for server in rack.servers:
                if server.view:
                    if server.virtualServers:
                        instancesExist = True
                        print("Server " + server.machineName + " is running the following: ")
                        for vServer in server.virtualServers:
                            print("Instance name: " + vServer.instanceName)
                            print("Image: " + vServer.image.imageName)
                            print("Flavor: " + vServer.flavor.size)
                            print()
        if not instancesExist:
            print("None")


# Evacuate rack
def adminEvacuateRack(rackName, racks = []):

    vServersToEvac = []
    vServersNotEvac = []

    for rack in racks:
        if rackName == rack.rackName:
            for server in rack.servers:
                if server.virtualServers:
                    for vServer1 in server.virtualServers:
                        vServersToEvac.append(vServer1)
                    del server.virtualServers [:] # Delete the virtual servers from the rack that is failing

    for vserver in vServersToEvac:
        print("Number of instances to evacuate: " + str(len(vServersToEvac)))
        print("Current vServer name: " + vserver.instanceName)

    for vServer in vServersToEvac:
        evacuated = False
        for rack in racks:
            if rack.rackName != rackName:
                for server in rack.servers:
                    print("Checking servers inside rack " + rack.rackName)
                    if server.unallocatedDisks >= vServer.vServerDisks:
                        print("Enough unallocated disks.")
                        if server.unallocatedMem >= vServer.vServerMem:
                            print("Enough unallocated memory.")
                            if server.unallocatedCores >= vServer.vServerCores:
                                print("Enough unallocated cores.")
                                evacuated = True
                                print("Evacuating to rack: " + rack.rackName)
                                print("To server: " + server.machineName)
                                server.virtualServers.append(vServer)
                                server.unallocatedCores -= vServer.vServerCores
                                server.unallocatedMem -= vServer.vServerMem
                                server.unallocatedDisks -= vServer.vServerDisks
                                if evacuated:
                                    break
                    if evacuated:
                        break
            if evacuated:
                break

        if not evacuated:
            vServersNotEvac.append(vServer)

    return vServersNotEvac


def adminRemoveServer(machinename, racks = []):
    for rack in racks:
        for server in rack.servers:
            if machinename == server.machineName:
                server.view = False


# Function to re-add machine that is not in view
def adminAddServer(newServer = Server(), racks = []):

    rackFound = False
    serverExists = False

    for rack in racks:
        if newServer.rackName == rack.rackName:
            rackFound = True
            for server in rack.servers:
                # Check if the server already exists in a rack
                if server.machineName == newServer.machineName:
                    if server.ip == newServer.ip:
                        serverExists = True
                        server.view = True  # Add the server back to system so it can be viewed

    if rackFound & serverExists:
        print("Server has been added to the system.")
    else:
        print("Machine for the specified information does not exist and has not been added to system.")