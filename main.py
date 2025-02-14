from azure_digital_twin.adt_client import AzureDigitalTwinClient
from azure_digital_twin.adt_service import AzureDigitalTwinsService


if __name__ == "__main__":
    dt_model = AzureDigitalTwinsService()
    models = dt_model.list_models()
    for model in models:
        model_data = model.as_dict()
        model_id = model_data.get("id")
        
        print(f"Model ID: {model_id}")


    # model_id = "dtmi:digitaltwins:isa95:BaseModel;1"
    # model = dt_model.get_model(model_id)
    # print(f"Model ID: {model}")

    # query_expression = "SELECT * FROM DIGITALTWINS"
    # dtwins = dt_model.query_digital_twins(query_expression)
    # print(f"DT : {dtwins}")
    # print(f"dir : {dir(dtwins)}")
    # print(f"DT by_page : {dtwins.by_page()}")
    # for dt in dtwins:
    #     print(f"DT for: {dt}")

    # for dt in dtwins.by_page():
    #     print(f"DT by page: {dir(dt)}")
    adt_service_client = AzureDigitalTwinClient()
    service_client = adt_service_client.client

    query_expression = 'SELECT * FROM DIGITALTWINS'
    query_result = service_client.query_twins(query_expression)
    print('DigitalTwins: ',query_result)

    
    
    all_twins = list(query_result)
    print('All Twins: ',all_twins)

    # Check if there are any results
    if all_twins:
        print(f'Found {len(all_twins)} twins')
        for twin in all_twins:
            print(twin)
    else:
        print('No twins found')

    # query_2 = "SELECT * FROM DIGITALTWINS WHERE IS_OF_MODEL = 'dtmi:digitaltwins:isa95:BaseModel;1'"
    # query_result = service_client.query_twins(query_2)
    # print('DigitalTwins: ',query_result)
    # all_twins = list(query_result)
    # print('All Twins2: ',all_twins)


    query_3 ="SELECT * FROM DIGITALTWINS WHERE Name = 'adt'"
    query_result = service_client.query_twins(query_3)
    all_twins = list(query_result)
    print('All Twins3: ',all_twins)
    

    query_4 = "SELECT * FROM DIGITALTWINS WHERE IS_OF_MODEL('dtmi:digitaltwins:isa95:BaseModel;1')"
    query_result = service_client.query_twins(query_4)
    all_twins = list(query_result)
    print('All Twins4: ',all_twins)


