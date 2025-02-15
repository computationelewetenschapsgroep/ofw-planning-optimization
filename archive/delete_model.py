import os
from azure.identity import DefaultAzureCredential
from azure.digitaltwins.core import DigitalTwinsClient



INSTANCE_NAME = os.getenv("ADT_INSTANCE_NAME")
endpoint = f"https://{INSTANCE_NAME}.api.neu.digitaltwins.azure.net"

credential = DefaultAzureCredential()

client = DigitalTwinsClient(endpoint, credential)

client.delete_model(model_id='dtmi:digitaltwins:isa95:Port;1')
