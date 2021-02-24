Block Layout Formation
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To decide how to place the clusters in the layout, the first step is to assign 
a priority to each cluster, based on the flows of materials between clusters 
(from-to chart). 
The fist clusters to be placed will be the ones with the highest flows, 
so that we can be sure to place them closer to each other.
On the contrary, clusters with low material flows can be assigned to the 
periphery of the plant layout, so they will enter last.

The algorithms implemented in this step are Punctual Flow, Total Flow and 
Weighted Flow.
In general, they will present different solutions to the user. 
Those solutions can be compared only in terms of costs, or the user can decide 
to accept a solution rather than another one because of various considerations 
about qualitative relations between clusters.

For example, placing a cluster in which hot material is processed next to a 
cluster that processes flammable material can be dangerous.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:From-to Chart: An *n*x*n* matrix where *n* is the number of unique types 
                of workshops or clusters. 
                Each element contains an integer representing the inbound or 
                outbound flows [travels/day] between a workshop or cluster and
                all the other ones.

:Qualitative relations matrix:  similar to the similarity matrix, it represents 
                                the qualitative relations between clusters (or 
                                workshops) for what regards qualitative 
                                characteristics like safety, communication 
                                needs with other clusters etc.

.. TO DEFINE!!

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Clusters insertion order:  An ordered list of clusters or workshops which 
                            represents the sequence of insertion of each cluster
                            in the layout.
