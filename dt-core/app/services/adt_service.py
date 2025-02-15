import os
from azure.identity import DefaultAzureCredential
from azure.digitaltwins.core import DigitalTwinsClient
from app.conf.configuration import settings

class ADTService:

    def __init__(self):
        endpoint = f"https://{settings.ADT_INSTANCE_NAME}.api.neu.digitaltwins.azure.net"
        credential = DefaultAzureCredential()

        self.client = DigitalTwinsClient(endpoint, credential)

adt_service = ADTService()        