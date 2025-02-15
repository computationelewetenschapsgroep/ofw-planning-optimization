from pydantic import BaseModel
from typing import List, Tuple

class Vessel(BaseModel):
    vessel_name: str
    vessel_location: str
    vessel_type: str
    day_rate: str
    responsibility: str
    
class Monopile(BaseModel):
    monopile_location: str 
    monopile_name: str

class Port(BaseModel):
    port_name: str
    port_layout: str
    port_location: str

class OffshoreWindFarm(BaseModel):
    site_name: str
    site_layout: str
    site_location: str
        

class FabricationYard(BaseModel):
    yard_name: str
    yard_layout: str
    yard_location: str


class Relation(BaseModel):
    relation_id: str
    source_twin: str
    relation_name: str
    target_twin: str

