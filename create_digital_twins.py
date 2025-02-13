import os
from azure.identity import DefaultAzureCredential
from azure.digitaltwins.core import DigitalTwinsClient



INSTANCE_NAME = os.getenv("ADT_INSTANCE_NAME")
endpoint = f"https://{INSTANCE_NAME}.api.neu.digitaltwins.azure.net"

credential = DefaultAzureCredential()

client = DigitalTwinsClient(endpoint, credential)

digital_twin_id = 'Vessel003'
temporary_twin = {
    "$metadata": {
        "$model": "dtmi:digitaltwins:isa95:Vessel;1"
    },
    "$dtId": digital_twin_id,  
    "description": {
        "$metadata": {
            "val" : "val"
        }    
    },
    "spatialDefinition": {
        "value": "UN/CEFACT CCTS",
        "$metadata": {

            "xyz": "dtmi:digitaltwins:isa95:SpatialDefinition;1"
        }
    } ,
    "tags": {
        "$metadata": {
            "abc": "abc"
        }
    }
}

created_twin = client.upsert_digital_twin(digital_twin_id, temporary_twin)
print(f'Created Digital Twin: {created_twin}')
