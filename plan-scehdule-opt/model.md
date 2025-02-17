Source Nodes are multiple

Sink node is 1 which is the final delivery site.  ( this is a simplification for now)

Constraint: All  assets have to arrive at the sink node at the same time window ( same day)
			     This is an assumption for now			

Nodes:
    1. Port
    2. Fabrication Yard
    3. Marshalling Yard
    4. Site                 

Edges: Activities 

		1. Mobilizing (M)
		2. Sailing  (S)
	    3. Loading (L)
		4. Storing (ST)
		5. Installing	 (I)	

Assumption :  
Stay at the Site (Fab Yard / Marshalling Yard only for Loading / Storing and no maintenance)

       Loops 
		1. Self loops ( L, ST, I)
		2. Cycles (L -> ST  -> L)


Costs:

	1. Edge Cost
			1. Sailing Time  (Fixed Cost, Assumption: We are not modeling uncertainty wrt to sailing time)
			2. Fuel Cost (Fixed  Cost)

    2. Node Cost: 
			1. Time  the vessel is at a site 
				a) Loading Cost
			    b)  Storing Cost
				c) Installation Cost		
                d) Idle Time Cost 

Edge Capacity:

        1. Carrying capacity (Non negative, Actiual capacity cannot exceed carrying  capacity)
Node Capacity:

        1. Storage capacity        
        
Demand:

      1. Number of monopiles to be installed at the site

Conservation:

	1. Wrt the vessel. What  goes into a now the same come out.

Decision Variables:

        1. Vessel State . One of [M, S, L , ST , I] . Binary vector where total sum is always equal to 1.
	    2. Vessel Availability (1/ 0)
        3. Vessel Capability  (to carry a monopile)
        4. Fabrication Yard Capacity (if the number of monopiles available is greater than threshold)
        5. The time the vessel is in a given state 
			

Constaint:

        1.  An activity should complete within a time bound . This is an edge constraint.
     

Vessels have individual responsibilities. For example one vessel transports monopile while the other transports the crane. 
However, during the installation process there are interdependencies for example the monopile cannot be offloaded from the transport vessel without the crane vessel. There  delivery cannot happen before all interdependencies are solved.




Schedule : Target Insatallation Date , D
Work needs to complete by target date D

For the work to be done 

	1.  Vessels have to follow a sequence of actions (traversal of a path from source to sink , with nodes & edges  + action on each node in between)

Objective: 

	Minimize the cost of completion of all actions 

Under the constraints defined above:



N = {Port, }