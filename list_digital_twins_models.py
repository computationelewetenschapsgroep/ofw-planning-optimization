import os
from azure.identity import DefaultAzureCredential
from azure.digitaltwins.core import DigitalTwinsClient

INSTANCE_NAME = os.getenv("ADT_INSTANCE_NAME")
endpoint = f"https://{INSTANCT_NAME}.api.neu.digitaltwins.azure.net"

credential = DefaultAzureCredential()

client = DigitalTwinsClient(endpoint, credential)

listed_models = client.list_models()
for model in listed_models:
    model_data = model.as_dict()
    model_id = model_data.get("id")
    model_description = model_data.get("description", {})
    description_text = model_description.get('en', "No Description Available")
    
    print(f"Model ID: {model_id}")
    print(f"Model Description: {description_text}")
    print("-" * 50)
