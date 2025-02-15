import os
from azure.identity import DefaultAzureCredential
from azure.digitaltwins.core import DigitalTwinsClient



INSTANCE_NAME = os.getenv("ADT_INSTANCE_NAME")
endpoint = f"https://{INSTANCE_NAME}.api.neu.digitaltwins.azure.net"

credential = DefaultAzureCredential()

client = DigitalTwinsClient(endpoint, credential)

digital_twin_id = 'Winchester'
temporary_twin = {
    "$metadata": {
        "$model": "dtmi:digitaltwins:isa95:Vessel;1"
    },
    "$dtId": digital_twin_id,  
    "description": {
        "$metadata": {
            "val" : "bokalift2"
        }    
    },
    "spatialDefinition": {
        "value": "POINT (0.00,0.00)",
        "format": "WKT",
        "$metadata": {
            "EPSG Code": "WGS 84",
            "model": "dtmi:digitaltwins:isa95:SpatialDefinition;1"
        }
    } ,
    "dayRate": "69750",
    "responsibility": "CraneTransport",
    "vesselType": "winchester",
    "equipmentLevel": "unit",
    "tags": {
        "$metadata": {
            "abc": "abc"
        }
    },
    "ID": "368006590"
}




created_twin = client.upsert_digital_twin(digital_twin_id, temporary_twin)
print(f'Created Digital Twin: {created_twin}')

digital_twin_id = 'Atlas'
temporary_twin = {
    "$metadata": {
        "$model": "dtmi:digitaltwins:isa95:Vessel;1"
    },
    "$dtId": digital_twin_id,  
    "description": {
        "$metadata": {
            "val" : "atlas"
        }    
    },
    "spatialDefinition": {
        "value": "POINT (0.00,0.00)",
        "format": "WKT",
        "$metadata": {
            "EPSG Code": "WGS 84",
            "model": "dtmi:digitaltwins:isa95:SpatialDefinition;1"
        }
    } ,
    "dayRate": "74440",
    "responsibility": "towing",
    "vesselType": "atlas",
    "equipmentLevel": "unit",
    "tags": {
        "$metadata": {
            "abc": "abc"
        }
    },
    "ID": "9413573"
}


created_twin = client.upsert_digital_twin(digital_twin_id, temporary_twin)
print(f'Created Digital Twin: {created_twin}')




digital_twin_id = 'Edinburgh'
temporary_twin = {
    "$metadata": {
        "$model": "dtmi:digitaltwins:isa95:Vessel;1"
    },
    "$dtId": digital_twin_id,  
    "description": {
        "$metadata": {
            "val" : "edinburg"
        }    
    },
    "spatialDefinition": {
        "value": "POINT (0.00,0.00)",
        "format": "WKT",
        "$metadata": {
            "EPSG Code": "WGS 84",
            "model": "dtmi:digitaltwins:isa95:SpatialDefinition;1"
        }
    } ,
    "dayRate": "79200",
    "responsibility": "mooring",
    "vesselType": "edinburg",
    "equipmentLevel": "unit",
    "tags": {
        "$metadata": {
            "abc": "abc"
        }
    },
    "ID": "9456757"
}


created_twin = client.upsert_digital_twin(digital_twin_id, temporary_twin)
print(f'Created Digital Twin: {created_twin}')
