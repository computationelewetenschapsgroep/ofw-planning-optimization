import os
from azure.identity import DefaultAzureCredential
from azure.digitaltwins.core import DigitalTwinsClient



INSTANCE_NAME = os.getenv("ADT_INSTANCE_NAME")
endpoint = f"https://{INSTANCE_NAME}.api.neu.digitaltwins.azure.net"

credential = DefaultAzureCredential()

client = DigitalTwinsClient(endpoint, credential)

#client.delete_relationship(digital_twin_id='Vessel001',relationship_id='04df9f2f-6ee2-4956-a60a-8e8470430791')

client.delete_digital_twin("Winchester")