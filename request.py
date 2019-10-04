import os

print("Welcom to GNS3 2 Autobot LAB ceator")
print("This is the list of possibe nodes ")

project = input("please enter a name for your Project :")

creat_project = ("curl -X POST \"http://localhost:3080/v2/projects\"" +
                 " -d \'{\"name\": \""+project+"\"}\'")
print(creat_project)
os.system(creat_project)


node_types = ["cloud", "ethernet_hub", "ethernet_switch",
              "nat", "vpcs", "virtualbox", "dynamips"]


for i in range(len(node_types)):
    print(node_types[i], end="\n")

found_node = False
while found_node == False:
    User_node = input("you choise please? >> ")

    for node in node_types:
        if User_node == node:
            found_node = True

    if found_node:
        node_types.append(User_node)
    else:
        print("Incorrect entry")
