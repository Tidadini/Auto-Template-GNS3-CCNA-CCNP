import os
import requests
import json

# request the GNS3 Server to get projects
r = requests.get("http://localhost:3080/v2/projects")
r.json()
print(r.json())

# put the responce from GNS3 Server in JSON file.
with open("person.json", "w") as json_file:
    json.dump(r.json(), json_file)

# read data from JSON file.
with open("person.json", "r") as myfile:
    data = myfile.read()
# parse file
print("project_ID:  " + obj[0]["project_id"])
myproject = str(obj[0]["project_id"])
print(myproject)

# send command to GNS3 Server : create VPC1 Node.
cmd_vpc1 = (
    "curl -i -X POST 'http://localhost:3080/v2/projects/"
    + myproject
    + "/nodes'"
    + ' -d \'{"compute_id": "local", "name": "vpc1", "node_type": "vpcs","x":10,"y":0,"z":10}\''
)
os.system(cmd_vpc1)

# send command to GNS3 Server : create VPC2 Node.
cmd_vpc2 = (
    "curl -i -X POST 'http://localhost:3080/v2/projects/"
    + myproject
    + "/nodes'"
    + ' -d \'{"compute_id": "local", "name": "vpc2", "node_type": "vpcs","x": 10,"y":100,"z":10}\''
)
os.system(cmd_vpc2)

# send command to GNS3 Server : create VPC3 Node.
cmd_vpc3 = (
    "curl -i -X POST 'http://localhost:3080/v2/projects/"
    + myproject
    + "/nodes'"
    + ' -d \'{"compute_id": "local", "name": "vpc3", "node_type": "vpcs","x": 10,"y":200,"z":10}\''
)
os.system(cmd_vpc3)

# send command to GNS3 Server : create VPC4 Node.
cmd_vpc4 = (
    "curl -i -X POST 'http://localhost:3080/v2/projects/"
    + myproject
    + "/nodes'"
    + ' -d \'{"compute_id": "local", "name": "vpc4", "node_type": "vpcs","x": 10,"y":300,"z":10}\''
)
os.system(cmd_vpc4)

# send command to GNS3 Server : create R1 Node.
cmd_R = (
    "curl http://localhost:3080/v2/projects/"
    + myproject
    + "/nodes"
    + ' -d \'{"symbol": ":/symbols/router.svg", "name": "R1", "properties": {"platform": "c7200", "nvram": 512, "image": "c7200-adventerprisek9-mz.152-4.M7.image", "ram": 512, "slot3": "PA-GE", "system_id": "FTX0945W0MY", "slot0": "C7200-IO-FE", "slot2": "PA-GE","slot4":"PA-GE", "slot1": "PA-GE",  "idlepc": "0x606e0538"}, "compute_id": "local", "node_type": "dynamips","x":-300,"y":150,"z":10}\''
)
os.system(cmd_R)

# request the GNS3 Server to get Nodes IDs
r1 = requests.get(
    "http://localhost:3080/v2/projects/" + obj[0]["project_id"] + "/nodes"
)
data = r1.json()
print(data)

with open("nodes.json", "w") as json_file:
    json.dump(r1.json(), json_file)

with open("nodes.json", "r") as myfile:
    data = myfile.read()
# parse file
obj = json.loads(data)
# show all node ID
for i in range(0,5):
    print("node_ID:  " + obj[i]["node_id"])

# send command to GNS3 Server : create link between R1--Pc1
PC1_R1 = (
    'curl -X POST  "http://localhost:3080/v2/projects/'
    + obj[0]["project_id"]
    + '/links"'
    + ' -d \'{"nodes": [{"adapter_number": 0, "node_id": "'
    + obj[0]["node_id"]
    + '", "port_number": 0}, {"adapter_number": 1, "node_id": "'
    + obj[4]["node_id"]
    + '", "port_number": 0}]}\''
)
os.system(PC1_R1)

# send command to GNS3 Server : create link between R1--Pc2
PC2_R1 = (
    'curl -X POST  "http://localhost:3080/v2/projects/'
    + obj[0]["project_id"]
    + '/links"'
    + ' -d \'{"nodes": [{"adapter_number": 0, "node_id": "'
    + obj[1]["node_id"]
    + '", "port_number": 0}, {"adapter_number": 2, "node_id": "'
    + obj[4]["node_id"]
    + '", "port_number": 0}]}\''
)
os.system(PC2_R1)

# send command to GNS3 Server : create link between R1--Pc3
PC3_R1 = (
    'curl -X POST  "http://localhost:3080/v2/projects/'
    + obj[0]["project_id"]
    + '/links"'
    + ' -d \'{"nodes": [{"adapter_number": 0, "node_id": "'
    + obj[2]["node_id"]
    + '", "port_number": 0}, {"adapter_number": 3, "node_id": "'
    + obj[4]["node_id"]
    + '", "port_number": 0}]}\''
)
os.system(PC3_R1)

# send command to GNS3 Server : create link between R1--Pc4
PC4_R1 = (
    'curl -X POST  "http://localhost:3080/v2/projects/'
    + obj[3]["project_id"]
    + '/links"'
    + ' -d \'{"nodes": [{"adapter_number": 0, "node_id": "'
    + obj[3]["node_id"]
    + '", "port_number": 0}, {"adapter_number": 4, "node_id": "'
    + obj[4]["node_id"]
    + '", "port_number": 0}]}\''
)
os.system(PC4_R1)

# Start Nodes
Start_PC1 = (
    'curl -X POST "http://localhost:3080/v2/projects/'
    + obj[0]["project_id"]
    + "/nodes/"
    + obj[0]["node_id"]
    + '/start" -d "{}"'
)
os.system(Start_PC1)

# Start Nodes
Start_PC2 = (
    'curl -X POST "http://localhost:3080/v2/projects/'
    + obj[0]["project_id"]
    + "/nodes/"
    + obj[1]["node_id"]
    + '/start" -d "{}"'
)
os.system(Start_PC2)

# Start Nodes
Start_PC3 = (
    'curl -X POST "http://localhost:3080/v2/projects/'
    + obj[0]["project_id"]
    + "/nodes/"
    + obj[2]["node_id"]
    + '/start" -d "{}"'
)
os.system(Start_PC3)

# Start Nodes
Start_PC4 = (
    'curl -X POST "http://localhost:3080/v2/projects/'
    + obj[0]["project_id"]
    + "/nodes/"
    + obj[3]["node_id"]
    + '/start" -d "{}"'
)
os.system(Start_PC4)


# Start Nodes
Start_R1 = (
    'curl -X POST "http://localhost:3080/v2/projects/'
    + obj[0]["project_id"]
    + "/nodes/"
    + obj[4]["node_id"]
    + '/start" -d "{}"'
)
