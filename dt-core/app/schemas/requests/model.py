from pydantic import BaseModel

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
    port_id: str
    port_name: str
    port_layout: str
    port_location: str

class OffshoreWindFarm(BaseModel):
    site_id: str
    site_name: str
    site_layout: str
    site_location: str
        

class FabricationYard(BaseModel):
    yard_id: str
    yard_name: str
    yard_layout: str
    yard_location: str
                