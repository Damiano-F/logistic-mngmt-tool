Assignment of products/parts to clusters
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the clusters are set, we have to decide which groups of parts or products 
to assign to each one of them.
The aim of this phase of the logistic optimization is to assign the products in 
a way that, in the ideal case, all the machining required to process a product 
can be executed inside one single cell.
This result can be difficult to achieve because the production cycle of a 
certain product may require to visit workshops that have been assigned to 
different clusters.
The tool applies an heuristic algorithm that takes into accountthe number of 
travels of parts inside the clusters, the number of machining inside the 
clusters and the times of machining inside the clusters to find an optimal 
solution.

The final result can be evaluated by a set of linear functions that serve 
as KPIs.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Part-machine incidence matrix ordered by clusters

:Production cycles:    for every product or part, the sequence of workshops 
                        visited and informations about the machining process, 
                        like the processing times

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Part-machine incidence matrix ordered by clusters and products assigned

* Key Performance Indicators of the part-machine incidence matrix ordered by 
  clusters and products assigned



