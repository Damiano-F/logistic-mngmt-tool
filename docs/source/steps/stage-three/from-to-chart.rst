From-to Chart Formation
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

With the clusters set, by knowing the flows of materials between workshops and 
vehices capacity, we can calculate the number of travels between each workshop.
The result can be represented as a matrix which shows the inbound and outbound
travels for each workshop. 
It should be read from rows to columns to understand the direction of the flows.

Because clusters are sets of workshops, it is possible to define the from-to 
chart between clusters as a sum of the flows of the workshops inside clusters.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Clusters of workshops: A set of clusters. Each cluster contains a set of
                        workshops.

:Production cycles: A list of sequences of machinings. Every sequence is the 
                    array of machinings required to complete a part or product.

:Daily demand:  A set of values representig the daily demand [pieces/day] of 
                parts/products.

:Bill of Materials: A set of raw materials and parts required to produce a 
                    finished product. 
                    Every entry reports both the type and the quantity of the 
                    materials required.

:Vehicles capacity: A set of integers representing for each category of vehicles
                    the number of pieces transported in a full-capacity travels
                    [pieces/travel] 

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:From-to Chart: An *n* x *n* matrix where *n* is the number of unique types 
                of workshops or clusters. 
                Each element contains an integer representing the inbound or 
                outbound flows [travels/day] between a workshop or cluster and
                all the other ones.
