import requests
import time

def add_subscriber():
    # SD-Core subscriber's provisioning api endpoint.
    url = "http://192.168.85.136:5000/api/subscriber/imsi-208930000000009"

    req_body = {
        "UeId":"208930000000009",
        "plmnId":"20893",
        "opc":"981d464c7c52eb6e5036234984ad0bcf",
        "key":"5122250214c33e723a5dd523fc145fc0",
        "sequenceNumber":"16f3b3f70fc2"
        }

    # Send POST
    response = requests.post(url,json=req_body)
    print(response)
    print(response.content)

def setup_subscriber():
    #Add imsi subscriber sim card and create a device
    sim_id = "aiab-sim-28"
    device_id = "aiab-ue-28"
    url = "http://localhost:31194/aether-roc-api/aether/v2.1.x/aiab-enterprise/site/aiab-site/sim-card/"+sim_id

    req_body = {
        "description": "sim card 28",
        "display-name": "UE 28 Sim",
        "enable": True,
        "imsi": "208930000000008",
        "sim-id": sim_id
        }

    print("Create sim card")
    response = requests.post(url, json=req_body)
    print(response.content)
    
    ###################################################################

    url = "http://localhost:31194/aether-roc-api/aether/v2.1.x/aiab-enterprise/site/aiab-site/device/"+device_id

    req_body = {
        "device-id": device_id,
        "display-name": "UE 28",
        "sim-card": sim_id,
        }

    print("Create device based on sim card")
    response = requests.post(url, json=req_body)
    print(response.content)

def assign_device_group():
    # Assign a device group to a device.
    dg_id = "dg4"
    device_id = "aiab-ue-28"
    url = "http://localhost:31194/aether-roc-api/aether/v2.1.x/aiab-enterprise/site/aiab-site/device-group/"+dg_id+"/device/"+device_id

    req_body = {
        "device-id": device_id,
        "enable": True
        }

    # Send POST
    print("Added to device group")
    response = requests.post(url, json=req_body)
    print(response.content)

def create_upf():
    upf_id = "upf4"
    url = "http://localhost:31194/aether-roc-api/aether/v2.1.x/aiab-enterprise/site/aiab-site/upf/"+upf_id

    req_body = {
        "address": "10.10.1.4",
        "config-endpoint": "http://10.10.1.4:8080",
        "description": "UPF for site3 slice 4",
        "display-name": "UPF 4",
        "port": 8805,
        "upf-id": upf_id,
        }

    # Send POST
    response = requests.post(url, json=req_body)
    print(response.content)

def create_slice():
    slice_id = "slice4"
    url = "http://localhost:31194/aether-roc-api/aether/v2.1.x/aiab-enterprise/site/aiab-site/slice/"+slice_id

    req_body = {
        "connectivity-service": "5g",
        "default-behavior": "ALLOW-ALL",
        "description": "Slice 4 for site 3",
        "device-group": [
            {
                "device-group": "dg4",
                "enable": True
            }
            ],
        "display-name": "slice 4",
        "mbr": {
            "downlink": 100000000,
            "downlink-burst-size": 625000,
            "uplink": 100000000,
            "uplink-burst-size": 625000
            },
        "sd": "040404",
        "slice-id": slice_id,
        "sst": "4",
        "upf": "upf4",
        }

    # Send POST
    response = requests.post(url, json=req_body)
    print(response)
    print(response.content)

def get_site():
    url = "http://localhost:31194/aether-roc-api/aether/v2.1.x/aiab-enterprise/site"
    response = requests.get(url)
    print(response)
    print(response.content)

print("Creating UPF")
#create_upf()

time.sleep(1)
print("Creating Slice")
#create_slice()

print("Adding subscriber")
#add_subscriber()

time.sleep(1)
print("Setting up subscriber")
#setup_subscriber()

print("Added device to device group")
#assign_device_group()

print("Get site description")
get_site()