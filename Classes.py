# This file contains the classes that I used in the project

# Rack class, a class to create a rack object to more easily keep track oof machines and other information
class Rack:

    def __set__(self, rackName, numMachines, storageCap, servers=[]):
        self.rackName = rackName
        self.numMachines = numMachines
        self.storageCap = storageCap
        self.servers = servers

    def __init__(self):
        self.rackName = ""
        self.numMachines = 0
        self.storageCap = 0
        self.servers = []

    def __eq__(self, other):

        equal = False

        my_rack_name = self.rackName
        my_num_machines = self.numMachines
        my_storage_cap = self.storageCap
        my_servers = self.servers

        his_rack_name = other.rackName
        his_num_machines = other.numMachines
        his_storage_cap = other.storageCap
        his_servers = other.servers

        if my_rack_name == his_rack_name:
            if my_num_machines == his_num_machines:
                if my_storage_cap == his_storage_cap:
                    if my_servers == his_servers:
                        equal = True

        return equal




# Server class to easily create Servers and keep track of them
class Server:

    view = True

    def __init__(self):
        self.machineName = ""  # name of the virtual machine
        self.rackName = ""  # rack where machine resides
        self.ip = ""  # ip address of the server
        self.mem = 0  # memory of the server
        self.numDisks = 0  # number of disks in the server
        self.numCores = 0  # number of cores in the server

        # Unallocated resources
        self.unallocatedMem = 0
        self.unallocatedDisks = 0
        self.unallocatedCores = 0

        self.virtualServers = []

    def __set__(self, machineName, rackName, ip, mem, numDisks, numCores):
        self.machineName = machineName
        self.rackName = rackName
        self.ip = ip
        self.mem = mem
        self.numDisks = numDisks
        self.numCores = numCores
        self.unallocatedMem = mem
        self.unallocatedDisks = numDisks
        self.unallocatedCores = numCores


# Flavor class to store flavors easier
class Flavor:

    def __init__(self):
        self.size = ""
        self.mem = 0
        self.numDisks = 0
        self.numCores = 0

    def __set__(self, size, mem, numDisks, numCores):
        self.size = size
        self.mem = mem
        self.numDisks = numDisks
        self.numCores = numCores

    def __eq__(self, other):
        equal = False

        my_size = self.size
        my_mem = self.mem
        my_disks = self.numDisks
        my_cores = self.numCores

        his_size = other.size
        his_mem = other.mem
        his_disks = other.numDisks
        his_cores = other.numCores

        if my_size == his_size:
            if my_mem == his_mem:
                if my_disks == his_disks:
                    if my_cores == his_cores:
                        equal = True

        return equal


# Create images to store them easily
class Image:

    def __init__(self):
        self.imageName = ""
        self.imageSizeMB = 0
        self.imagePath = ""

    def __set__(self, imageName, imageSizeMB, imagePath):
        self.imageName = imageName
        self.imageSizeMB = imageSizeMB
        self.imagePath = imagePath

    def __eq__(self, other):

        equal = False

        my_image_name = self.imageName
        my_image_sizeMB = self.imageSizeMB
        my_image_path = self.imagePath

        his_image_name = other.imageName
        his_image_sizeMB = other.imageSizeMB
        his_image_path = other.imagePath

        if my_image_name == his_image_name:
            if my_image_sizeMB == his_image_sizeMB:
                if my_image_path == his_image_path:
                    equal = True

        return equal



# Virtual servers that will be created in the physical servers
class virtualServer:

    def __init__(self):
        self.instanceName = ""
        self.vServerDisks = 0
        self.vServerMem = 0.0
        self.vServerCores = 0
        self.image = Image()
        self.flavor = Flavor()

    def __set__(self, instanceName, vServerDisks, vServerMem, vServerCores, image=Image(), flavor=Flavor()):
        self.instanceName = instanceName
        self.vServerDisks = vServerDisks
        self.vServerMem = vServerMem
        self.image = image
        self.vServerCores = vServerCores
        self.flavor = flavor

    def __eq__(self, other):

        equal = False

        my_instance_name = self.instanceName

        his_instance_name = other.instanceName

        if my_instance_name == his_instance_name:
            equal = True

        return equal

