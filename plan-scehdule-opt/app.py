import streamlit as st
from model import VesselName, VesselRole , Vessel
from model import Node, Edge, FlowGraph, LocationType, ActivityType
from shapely import Point
from typing import List
#from pyvis.network import Network
import streamlit.components.v1 as components
import pandas as pd
import networkx as nx
import datetime
from algo import DecisionModel, nextmv, nextroute
from model import sample_input
import json

parameters = []

default_options = nextroute.Options()
for name, default_value in default_options.to_dict().items():
    parameters.append(nextmv.Parameter(name.lower(), type(default_value), default_value, name, False))

options = nextmv.Options(*parameters)

model = DecisionModel()

today = datetime.datetime.now()

if 'vessels' not in st.session_state:
    st.session_state.vessels: List[Vessel] = []

if 'activity_graph' not in st.session_state:
    st.session_state.flow_graph = FlowGraph()

if 'nodes' not in st.session_state:
    st.session_state.nodes: List[Node] = []

if 'edges' not in st.session_state:
    st.session_state.edges: List[Edge] = []

if 'schedule' not in st.session_state:
    st.session_state.schedule = pd.DataFrame(
        [
            {"Monopile ID":"M1.1001","Availability Date": today , "Installation Date": today + datetime.timedelta(weeks=+4)},
        ]
    )

if 'genPlan' not in st.session_state:
    st.session_state.genPlan = pd.DataFrame(
        [
            {"Vessed ID":"V1.1001","Stops Id": "Port 1.1001" , "Latitude": 0.0, "Longitude": 0.0, "Arrival Time": today, "Total Travel Duration": 0.0, "End Time": today, "Start Time": today,  "Travel Duration": 0.0, "Travel Distance": 0.0},
        ]
    )

def add_vessel(type, role, 
               latitude,
               longitude, 
               capacity, 
               availability,
               speed,
               start_date,
               end_date):
    st.session_state.vessels.append(Vessel(
        vessel_type=type,
        vessel_role=role,
        latitude = latitude,
        longitude=longitude,
        transport_capacity=capacity,
        availability=availability,
        speed = speed,
        start_date=start_date,
        end_date=end_date
    ))

def add_nodes(location_type, 
              location_id,
              location_name,
              latitude,
              longitude,
              location_capacity,
              location_demand):
    st.session_state.nodes.append( Node(type = location_type,
                id = location_id,
                name = location_name,
                latitude = latitude,
                longitude= longitude,
                capacity = location_capacity,
                demand= location_demand)
    )   
    
    #st.session_state.flow_graph.add_node(node)      

def add_edges(
        activity_type,
        activity_duration,
        unit_cost,
        source_node,
        target_node
):
    st.session_state.edges.append( Edge(type = activity_type,
                activity_duration = activity_duration,
                unit_cost = unit_cost,
                source = source_node,
                target = target_node)
    )    
    #st.session_state.flow_graph.add_edge(edge)  

def run_planner():
    st.session_state.genPlan.drop(st.session_state.genPlan.index, inplace=True)
    unique_vessels: List[Vessel] = []
    for vessel in  st.session_state.vessels:
        if vessel.latitude == 0.0 or vessel.longitude == 0.0:
            continue
        if vessel.vessel_type.name not in list(map(lambda item: item.vessel_type.name ,unique_vessels)):
            unique_vessels.append(vessel)
    sample_input["vehicles"] = []  
          
    for vessel in unique_vessels:
        sample_input["vehicles"].append(
            {
                "id": vessel.vessel_type.name,
               "start_location": {
                   "lon": vessel.longitude,
                   "lat": vessel.latitude
               } ,
               "start_time": vessel.start_date.strftime("%Y-%m-%dT%H:%M:%S-%H:%M"),
               "end_time": vessel.end_date.strftime("%Y-%m-%dT%H:%M:%S-%H:%M"),
               "capacity": vessel.transport_capacity
            }
        )
    
    stops: List[Node] = []
    for node in st.session_state.nodes:
        if node.latitude == 0.0 or node.longitude == 0.0:
            continue
        if node.id not in list(map(lambda item: item.id, stops)):
            stops.append(node)
    sample_input["stops"] = []
    for stop in stops:
         sample_input["stops"].append({
             "id": stop.id,
             "name": stop.name,
             "location": {
                 "lon": stop.longitude,
                "lat": stop.latitude
             },
             "demand": stop.demand,
             "duration": 0
         })
   
    
    for edge in st.session_state.flow_graph.edges:
            source, target = edge
            print(st.session_state.flow_graph.edges[source,target])
            for stop in  sample_input["stops"]:
                if source == target:
                    stop["duration"] += st.session_state.flow_graph.edges[source,target]["duration"]*3600
                    continue
                if stop["name"] == target:
                    stop["succeeds"] = st.session_state.flow_graph.nodes[source]["id"]

    print(sample_input)    
    input = nextmv.Input(data=sample_input, options=options)
    output = model.solve(input)
    print(output) 
    for elem in output.solution['vehicles']:
        route_travel_distance = 0.0
        if 'route_travel_distance' in elem.keys():
            route_travel_distance = elem['route_travel_distance'] / 1000
        for route in elem['route']:
            st.session_state.genPlan.loc[len(st.session_state.genPlan)] = [elem['id'], 
                                                                               route['stop']['id'],
                                                                               route['stop']['location']['lat'],
                                                                               route['stop']['location']['lon'],
                                                                               route['arrival_time'],
                                                                               route['cumulative_travel_duration'],
                                                                               route['end_time'],
                                                                               route['start_time'],
                                                                               route['travel_duration']/3600,
                                                                               route_travel_distance
                                                                               ]

st.title("Orsted PROSIM Scenario Generation")

with st.form("Vessel"):
    st.write("Add Vessel Details")
    vessel_type = st.radio("Choose Vessel Type",
                        [VesselName.ATLAS.name, 
                        VesselName.BOKALIFT.name,
                        VesselName.EDINBURG.name, 
                        VesselName.WINCHESTER.name])

    

    vessel_role = st.radio("Choose Vessel Role",
                        [VesselRole.INSTALLATION.name,
                        VesselRole.TRANSPORT.name,
                        VesselRole.INSTALLATION.name])
    
    latitude = st.text_input("Latitude", "0.0")
    longitude = st.text_input("Longitude", "0.0")


    capacity = st.text_input("Monopile Transport Capacity", "0")


    vessel_availability = st.radio("Choose Vessel Availability",
                        [True,
                            False])
    
    speed = st.text_input("Vessel Speed", "0.0")

    start_date = st.date_input("Vessel Start Time")
    end_date = st.date_input("Vessel End Time")

    st.form_submit_button("Add Vessel",
                          on_click=add_vessel,
                          args=(VesselName[vessel_type],
                                VesselRole[vessel_role],
                                float(latitude),
                                float(longitude),
                                int(capacity),
                                bool(vessel_availability),
                                speed,
                                start_date,
                                end_date),
                                )
        

st.write(st.session_state.vessels)

with st.form("Locations"):
    st.write("Add Location Details")

    location_type = st.radio("Choose Location Type",
                        [LocationType.PORT.name, 
                         LocationType.FABRICATION_YARD.name,
                        LocationType.MARSHALLING_YARD.name, 
                        LocationType.OFFSHORE_WIND_FARM.name])
    
    id = st.text_input("Identifier","L001")
    name = st.text_input("Name","Argentia")

    latitude = st.text_input("Latitude", "0.0")
    longitude = st.text_input("Longitude", "0.0")


    capacity = st.text_input("Location Capacity", "0")


    demand = st.text_input("Location demand", "0")

    

    st.form_submit_button("Add Location", on_click=add_nodes,
                          args=(LocationType[location_type],
                                id,
                                name,
                                latitude,
                                longitude,
                                int(capacity),
                                int(demand)))

with st.form("Activities"):
    st.write("Add Activity Details")
    activity_type = st.radio("Choose Activity Type",
                        [ActivityType.DOCKED.name, 
                         ActivityType.SAILING.name,
                        ActivityType.STORING.name, 
                        ActivityType.MOBILIZING.name,
                        ActivityType.LOADING.name,
                        ActivityType.INSTALLING.name])
    
    source = st.text_input("Source Name","Argentia")
    target = st.text_input("Target Name","Ofw/US")
    activity_duration = st.text_input("Activity Duration (hrs)", "0.0")
    unit_cost = st.text_input("Cost per hour", "0.0")
    st.form_submit_button("Add Activity", on_click= add_edges,
                          args=(ActivityType[activity_type],
                                float(activity_duration),
                                float(unit_cost),
                                source,
                                target))
                        

st.write(st.session_state.nodes)
st.write(st.session_state.edges)

with st.form("Flow Graph"):
    st.write("Build  Flow Graph")
    if st.form_submit_button("Create"):
        st.session_state.flow_graph = FlowGraph(nodes = st.session_state.nodes,
                                                edges = st.session_state.edges)
        df = nx.to_pandas_adjacency(st.session_state.flow_graph)
        st.dataframe(df, use_container_width=True)
       

with st.form("Add Schedule"):
    st.write("Create Installation Schedule")
    edited_df = st.data_editor(st.session_state.schedule, num_rows="dynamic")
    st.form_submit_button("Run Planner", on_click=run_planner)


st.write("Generated Plan")
st.dataframe(st.session_state.genPlan,use_container_width=True)
