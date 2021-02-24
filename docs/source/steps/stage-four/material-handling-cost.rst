Cost of Material Handling 
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the phisical layout and the handling equipment are set, it's possible to 
measure the distances between clusters and the times of every travel, 
comprehensive of the times for the loading and unloading of the vehicles.

It is also possible to decide how much space to allocate to the storage of 
pallets in the plant.
With the information about the specific costs of travelling in [€/meter] or 
[€/minute], it is possible to calculate the cost of material handling.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:From-to Chart: An *n*x*n* matrix where *n* is the number of unique types 
                of workshops or clusters. 
                Each element contains an integer representing the inbound or 
                outbound flows [travels/day] between a workshop or cluster and
                all the other ones.

:Storage areas: A set of values representing for each kind of machine the 
                storage area [m^2] disposable around it.

:Informations about the vehicles:   A set associating to each kind of vehicle
                                    the values of speed, acceleration, 
                                    deceleration, up-times [%], load/unload 
                                    times, pallets capacity [pallets/vehicle], 
                                    costs in [€/m] or [€/minute].

:Area of a pallet: The area [m^2] occupied by one pallet.

:Shifting schedulation: A set of integer values representing the shifts per day 
                        [shifts/day] for material handling operations.

:Shift duration: The length of a shift in [hours].

:Pauses:    A set of values representing the time lost for pauses during a shift 
            [min/shift] for material handling operations. 

:Up-time %: A set of values representing the % of time in which each kind of 
            vehicle is operational. 
            Down times can occur because of vehicles failures or maintenance.

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Total material handling costs: A value [€/day] which represents the cost of
                                material handling operations necessary to 
                                complete the daily production.

:Travel costs matrix:   An *n*x*n* matrix where *n* is the number of unique 
                        types of workshops or clusters. 
                        Each element contains a value representing the cost of
                        one travel from and to a cluster or workshop and all
                        the other ones.
                        
:Number of vehicles:    A set of integers representing, for each kind 
                        of vehicle, the dimension of the fleet needed to sustain
                        the daily material handling operations.

:Total travel time: A value [min/day] representing the total travelling time
                    of all the parts and products in one day.

:Total distances:   A value [m/day] representing the total travelling distance
                    of all the parts and products in one day.

:Material handling KPIs:    A set of KPIs for the evaluation of traffic and 
                            disposable areas.