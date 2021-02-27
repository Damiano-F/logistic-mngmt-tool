Evaluation of Machines Duplication Options
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To reduce the cost of material handling, it can be convenient to add some 
machines inside clusters. 
This choice causes an increment of fixed costs due to the purchasing of 
additional machines, but a decrease of variable costs due to the terminated 
flows of materials between clusters.
The machines that are most convenient to duplicate are the ones most involved in 
the flows from or to machines located in other clusters.
The aim of the algorithm is to find the optimal balance between fixed and 
variable costs, or in other words to decide which machines to duplicate and 
where.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:From-to Chart: An *n* x *n* matrix where *n* is the number of unique types 
                of workshops. 
                Each element contains an integer representing the inbound or 
                outbound flows [travels/day] between a workshop and
                all the other ones.

..note::    we are evaluating the impact of the duplication of single machines 
            inside clusters, so the change in the flow of material have to be 
            evaluated by single machines and not from cluster to cluster.

:Diagonalized PMIM: A *n* x *m* matrix where *n* is the number of unique types of 
                    workshops and *m* is the number of different parts. 

                    Each element of the matrix may contain:

                    - 1 if the product visits the corresponding workshop
                    - 0 otherwise.

                    The *n* workshops have been reordered according to the sets
                    of clusters.
                    The *m* parts have been reordered according to parts 
                    assignment.

..note::    This time we take the composition of clusters into account to 
            differenciate between inside-cell flows and outside-cell flows.
            We only need to consider the latter.

:Machines costs:    A set of values [€] associating to each kind of machine its
                    purchasing cost.

:Travel costs matrix:   An *n* x *n* matrix where *n* is the number of unique 
                        types of workshops or clusters. 
                        Each element contains a value representing the cost of
                        one travel from and to a cluster or workshop and all
                        the other ones.

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:New clusters of workshops: A set of clusters. Each cluster contains a set of
                            workshops, including the newly added mmachines.

:New diagonalized PMIM: A *n* x *m* matrix where *n* is the number of unique types 
                        of workshops and *m* is the number of different parts. 

                        Each element of the matrix may contain:

                        - 1 if the product visits the corresponding workshop
                        - 0 otherwise.

                        The *n* workshops have been reordered according to the 
                        sets of new clusters.
                        The *m* parts have been reordered according to parts 
                        assignment.

:New total material handling costs: A value [€/day] which represents the cost of
                                    material handling operations necessary to 
                                    complete the daily production, according to
                                    the new clusters.



