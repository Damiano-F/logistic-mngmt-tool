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
The tool applies an heuristic algorithm that takes into account the number of 
travels of parts inside the clusters, the number of machining inside the 
clusters and the times of each machining inside the clusters to find an optimal 
solution.

The final result can be evaluated by a set of linear functions that serve 
as KPIs.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Clustered PMIM:  A *n*x*m* matrix where *n* is the number of unique types of 
                  workshops and *m* is the number of different parts. 

                  Each element of the matrix may contain:

                  - 1 if the product visits the corresponding workshop
                  - 0 otherwise.

                  The *n* workshops have been reordered according to the sets
                  of clusters.

:Production cycles: A list of sequences of machinings. Every sequence is the 
                    array of machinings required to complete a part or product. 
                    Every single element of the array contains a set of 
                    machining times and operator times required to process one 
                    unit of the respective product.

..note::  The role of the setup times in the assigment of parts to clusters
          is to be clarified.

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Diagonalized PMIM: A *n*x*m* matrix where *n* is the number of unique types of 
                    workshops and *m* is the number of different parts. 

                    Each element of the matrix may contain:

                    - 1 if the product visits the corresponding workshop
                    - 0 otherwise.

                    The *n* workshops have been reordered according to the sets
                    of clusters.
                    The *m* parts have been reordered according to parts 
                    assignment.

:Diagonalized PMIM KPSs:  A set of indexes wich evaluate the quality of the 
                          diagonalized PMIM.



