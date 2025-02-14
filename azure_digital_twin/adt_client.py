from azure.identity import DefaultAzureCredential
from azure.digitaltwins.core import DigitalTwinsClient
from typing import Optional
from settings import settings

from utils.singleton import singleton

@singleton
class AzureDigitalTwinClient:
    """ Class for interacting with the Azure Digital Twins client. """

    def __init__(self, credential: Optional[DefaultAzureCredential] = None):
        """
        Singleton class for initializing the DtClient with configuration and credentials.

        :param credential: Azure credentials for authentication (DefaultAzureCredential if None).
        """
        self.credential = credential or DefaultAzureCredential()
        self.client = self._create_client()

    def _create_client(self) -> DigitalTwinsClient:
        """ Creates and returns a DigitalTwinsClient instance. """
        return DigitalTwinsClient(settings.adt_endpoint, self.credential)
    
