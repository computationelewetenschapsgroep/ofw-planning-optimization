import os
from azure.identity import DefaultAzureCredential
from azure.digitaltwins.core import DigitalTwinsClient



INSTANCE_NAME = os.getenv("ADT_INSTANCE_NAME")
endpoint = f"https://{INSTANCE_NAME}.api.neu.digitaltwins.azure.net"

credential = DefaultAzureCredential()

client = DigitalTwinsClient(endpoint, credential)

digital_twin_id = 'Vessel001'
temporary_twin = {
    "$metadata": {
        "$model": "dtmi:digitaltwins:isa95:Vessel;1"
    },
    "$dtId": digital_twin_id
}

created_twin = client.upsert_digital_twin(digital_twin_id, temporary_twin)
print('Created Digital Twin:')
print(created_twin)