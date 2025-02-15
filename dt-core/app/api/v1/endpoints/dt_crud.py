from fastapi import APIRouter, Request, Response
from uvicorn.main import logger
from app.conf.configuration import settings
from starlette import status
from app.schemas.requests.model import Vessel, Monopile, OffshoreWindFarm, FabricationYard, Port, Relation
from app.services.adt_service import adt_service
from typing import List

router = APIRouter()


@router.put("/dt/vessels/{vessel_id}",status_code=status.HTTP_200_OK)
async def create_vessel_dt(vessel_id: str, vessel: Vessel):
    vessel_twin = {
    "$metadata": {
        "$model": "dtmi:digitaltwins:isa95:Vessel;1"
    },
    "$dtId": vessel.vessel_name,  
    "description": {
        "$metadata": {
            "val" : vessel.vessel_name
        }    
    },
    "spatialDefinition": {
        "value": vessel.vessel_location,
        "format": "WKT",
        "$metadata": {
            "EPSG Code": "WGS 84",
            "model": "dtmi:digitaltwins:isa95:SpatialDefinition;1"
        }
    } ,
    "dayRate": vessel.day_rate,
    "responsibility": vessel.responsibility,
    "vesselType": vessel.vessel_type,
    "equipmentLevel": "unit",
    "tags": {
        "$metadata": {
            "abc": "abc"
        }
    },
        "ID": vessel_id
    }
    created_twin = adt_service.client.upsert_digital_twin(vessel_id, vessel_twin)
    logger.info(f'Created Digital Twin: {created_twin}')
    return created_twin




@router.get("/dt/vessels/{vessel_id}",status_code=status.HTTP_200_OK)
async def read_vessel_dt(vessel_id: str):
    return adt_service.client.get_digital_twin(vessel_id)

@router.delete("/dt/vessels/{vessel_id}", status_code=status.HTTP_200_OK)
async def delete_vessel_dt(vessel_id: str):
    deleted_twin = adt_service.client.delete_digital_twin(vessel_id)
    return deleted_twin


@router.put("/dt/monopiles/{monopile_id}",status_code=status.HTTP_200_OK)
async def create_monopile_dt(monopile_id: str, monopile: Monopile):
    monopile_twin =  {
    "$metadata": {
        "$model": "dtmi:digitaltwins:isa95:Monopile;1"
    },
    "$dtId": monopile_id,  
    "tags": {
        "$metadata": {
            "abc": "aa"
        }
    },
    "equipmentLevel": "unit",
    "spatialDefinition": {
        "value": monopile.monopile_location,
        "format": "WKT",
        "$metadata": {
            "EPSG Code": "WGS 84",
            "model": "dtmi:digitaltwins:isa95:SpatialDefinition;1"
        }
    },
    "description": {
        "$metadata": {
            "val" : monopile.monopile_name
        }    
    },

        "ID": monopile_id
    }
    created_twin = adt_service.client.upsert_digital_twin(monopile_id, monopile_twin)
    logger.info(f'Created Digital Twin: {created_twin}')
    return created_twin



@router.get("/dt/monopiles/{monopile_id}",status_code=status.HTTP_200_OK)
async def read_monopile_dt(monopile_id: str):
    return adt_service.client.get_digital_twin(monopile_id)


@router.delete("/dt/monopiles/{monopile_id}",status_code=status.HTTP_200_OK)
async def delete_monopile_dt(monopile_id: str):
    deleted_twin = adt_service.client.delete_digital_twin(monopile_id)
    return deleted_twin


@router.get("/dt/relations/{digital_twin_id}",status_code=status.HTTP_200_OK)
async def get_relations(digital_twin_id: str):
    relationships  = adt_service.client.list_relationships(digital_twin_id)
    return  [rel for rel in relationships]

@router.put("/dt/connect/",status_code=status.HTTP_200_OK)
async def connect_twins(relationships: List[Relation] ):
    payload = []
    for relation in relationships:
        payload.append(
            {
                "$relationshipId": relation.relation_id,
                "$sourceId": relation.source_twin,
                "$relationshipName": relation.relation_name,
                "$targetId": relation.target_twin
            }
        )
    logger.info(f"payload: {payload}")
    for relationship in payload:
        adt_service.client.upsert_relationship(relationship["$sourceId"], 
                                           relationship["$relationshipId"], 
                                           relationship)


@router.delete("/dt/relations/{twin_id}/{relation_id}", status_code=status.HTTP_200_OK)
async def delete_relation(twin_id: str ,relation_id: str):
    adt_service.client.delete_relationship(twin_id, relation_id)


@router.put("/dt/ports/{port_id}",status_code=status.HTTP_200_OK)
async def create_port_dt(port_id: str, port: Port):
    port_twin =  {
    "$metadata": {
        "$model": "dtmi:digitaltwins:isa95:Port;1"
    },
    "$dtId": port_id,  
    "tags": {
        "$metadata": {
            "abc": "aa"
        }
    },

    "spatialDefinition": {
        "value": port.port_location,
        "format": "WKT",
        "$metadata": {
            "EPSG Code": "WGS 84",
            "model": "dtmi:digitaltwins:isa95:SpatialDefinition;1"
        }
    }
    }
    created_twin = adt_service.client.upsert_digital_twin(port_id, port_twin)
    logger.info(f'Created Digital Twin: {created_twin}')
    return created_twin


@router.get("/dt/ports/{port_id}",status_code=status.HTTP_200_OK)
async def read_port_dt(port_id: str):
    return adt_service.client.get_digital_twin(port_id)

@router.delete("/dt/ports/{port_id}",status_code=status.HTTP_200_OK)
async def delete_port_dt(port_id: str):
    adt_service.client.delete_digital_twin(port_id)


@router.put("/dt/ofw/{ofw_id}",status_code=status.HTTP_200_OK)
async def create_ofw_dt(ofw_id: str, offshore_wind_farm: OffshoreWindFarm):
    ofw_twin =  {
    "$metadata": {
        "$model": "dtmi:digitaltwins:isa95:OffshoreWindFarm;1"
    },
    "$dtId": ofw_id,  
    "tags": {
        "$metadata": {
            "abc": "aa"
        }
    },

    "spatialDefinition": {
        "value": offshore_wind_farm.site_location,
        "format": "WKT",
        "$metadata": {
            "EPSG Code": "WGS 84",
            "model": "dtmi:digitaltwins:isa95:SpatialDefinition;1"
        }
    }
    }
    created_twin = adt_service.client.upsert_digital_twin(ofw_id, ofw_twin)
    logger.info(f'Created Digital Twin: {created_twin}')
    return created_twin


@router.get("/dt/ofw/{ofw_id}",status_code=status.HTTP_200_OK)
async def read_ofw_dt(ofw_id: str):
     return adt_service.client.get_digital_twin(ofw_id)


@router.delete("/dt/ofw/{ofw_id}",status_code=status.HTTP_200_OK)
async def delete_ofw_dt(ofw_id: str):
    adt_service.client.delete_digital_twin(ofw_id)


@router.put("/dt/yards/{yard_id}",status_code=status.HTTP_200_OK)
async def create_yard_dt(yard_id: str, fabrication_yard: FabricationYard):
    fab_yard_twin =  {
    "$metadata": {
        "$model": "dtmi:digitaltwins:isa95:FabricationYard;1"
    },
    "$dtId": yard_id,  
    "tags": {
        "$metadata": {
            "abc": "aa"
        }
    },

    "spatialDefinition": {
        "value": fabrication_yard.yard_location,
        "format": "WKT",
        "$metadata": {
            "EPSG Code": "WGS 84",
            "model": "dtmi:digitaltwins:isa95:SpatialDefinition;1"
        }
    }
    }
    created_twin = adt_service.client.upsert_digital_twin(yard_id, fab_yard_twin)
    logger.info(f'Created Digital Twin: {created_twin}')
    return created_twin


@router.get("/dt/yards/{yard_id}",status_code=status.HTTP_200_OK)
async def read_yard_dt(yard_id: str):
    return adt_service.client.get_digital_twin(yard_id)

@router.delete("/dt/yards/{yard_id}",status_code=status.HTTP_200_OK)
async def delete_yard_dt(yard_id: str):
    adt_service.client.delete_digital_twin(yard_id)


