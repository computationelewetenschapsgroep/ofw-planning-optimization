from pydantic import BaseModel
from abc import ABCMeta
from  networkx import DiGraph
from typing import Union
from enum import Enum
from datetime import datetime

class LocationType(Enum):
    PORT=1
    FABRICATION_YARD=2
    MARSHALLING_YARD=3
    OFFSHORE_WIND_FARM=4

class ActivityType(Enum):
    DOCKED=1
    MOBILIZING=2
    SAILING=3
    LOADING=4
    STORING=5
    INSTALLING=6


class VesselName(Enum):
    EDINBURG=1
    ATLAS=2
    WINCHESTER=3
    BOKALIFT=4

class VesselRole(Enum):
    TRANSPORT = 1
    INSTALLATION = 2 
    LIFT = 3

class Node(BaseModel):
    type: LocationType
    id: str
    name: str 
    latitude: float
    longitude: float 
    capacity: int
    demand: int
    
    class Config:
        arbitrary_types_allowed=True

class Edge(BaseModel):
    type: ActivityType
    activity_duration: float 
    unit_cost: float
    source: str
    target: str

    class Config:
        arbitrary_types_allowed=True

class Vessel(BaseModel):
    vessel_type: VesselName
    vessel_role: VesselRole
    latitude: float
    longitude: float
    transport_capacity: int
    availability: bool
    #status: Union[Mobilizing, Sailing, Loading, Storing, Installing, Waiting]
    start_date: datetime
    end_date: datetime
    speed : float

    class Config:
        arbitrary_types_allowed=True


class FlowGraph(DiGraph):
    """
    class to define and solve minimum cost flow problems
    """
    def __init__(self, nodes=[], edges=[]):
        """
        initialize FlowGraph object
        :param nodes: list of nodes
        :param edges: list of edges
        """
        # initialialize digraph
        super().__init__(None)

        # add nodes and edges
        for node in nodes: self.add_node(node)
        for edge in edges: self.add_edge(edge)


    def add_node(self, node):
        """
        add node to graph
        :param node: Node object
        """
        # check if node is a Node object
        if not isinstance(node, Node): raise ValueError('node must be a Node object')
        # add node to graph
        super().add_node(node.name, type=node.type, 
                         id = node.id,
                         capacity=node.capacity, 
                         demand=node.demand, 
                         latitude=node.latitude,
                         longitude = node.longitude)
        
    
    def add_edge(self, edge):    
        """
        add edge to graph
        @param edge: Edge object
        """   
        # check if edge is an Edge object
        if not isinstance(edge, Edge): raise ValueError('edge must be an Edge object')
        # check if nodes exist
        if not edge.source in super().nodes: return
        if not edge.target in super().nodes: return

        # add edge to graph
        super().add_edge(edge.source, edge.target, 
        duration =edge.activity_duration, 
        unit_cost=edge.unit_cost, 
        type=edge.type)






sample_input = {
  "defaults": {
    "vehicles": {
      "speed": 34.44
    }
  },
  "stops": [
    {
      "id": "s1",
      "location": {
        "lon": -53.4705111,
        "lat":  47.5837027
      },
      "compatibility_attributes": ["premium"]
    },
    {
      "id": "s2",
      "location": {
        "lon": 11.9139664,
        "lat":  54.2977437
      },
      "compatibility_attributes": ["premium"],
      "succeeds": "s1"
    }
  ],
  "vehicles": [
    {
      "id": "vessel-0",
      "start_time": "2025-02-15T06:00:00-06:00",
      "end_time": "2025-03-17T10:00:00-06:00",
      "activation_penalty": 4000,
      "compatibility_attributes": ["premium"]
    },
    {
      "id": "vessel-1",
      "start_time": "2025-02-15T10:00:00-06:00",
      "end_time": "2025-03-17T16:00:00-06:00",
      "compatibility_attributes": ["basic"]
    }
  ]
}
