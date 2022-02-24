from userClass import User
from objectClass import Object
from custDict import cust_dict
# import numpy

subDict= cust_dict()
objDict = cust_dict()
wList = list() # not sure if i need this

fileReadin = open("actions.txt", "r")
lines = fileReadin.readlines()
fileReadin.close()
my_list = ["addsub", "addobj", "status\n", "write", "read"]

# here the whole read-in sentence is being treated as a string. However, each split that happens occupies
# a different index, so if the line is an addsub action, addsub will be at i = 0, the euid at i = 1, and
# the priority at i = 2

for line in lines:

    line = line.split(" ")

    # the following lines will do different actions depending on what the action was in the actions.txt file
    # line[0] is the action that is to be done.

    if line[0] == my_list[0]:    # addsub
        newUser = User(line[1])
        subDict.add(newUser.getName(), line[2])
        # i could just use line[1] but this way we ensure the
        # object and the map have the same value
        print(subDict) # this shows the key value pairs with name : level pairs

    elif line[0] == my_list[1]:  # addobj
        print(line[0])

    elif line[0] == my_list[2]:  # status
        print("status")

    elif line[0] == my_list[3]:  # write
        print(line[0])

    elif line[0] == my_list[4]:  # read
        print(line[0])

# newUser = User()
# newObj = Object()