Evaluation of Machines Duplication Options
-------------------------------------------

Context
~~~~~~~~~~~~

To reduce the cost of material handling, it can be convenient to add some machines inside clusters. 
This choice causes an increment of fixed costs due to the purchasing of additional machines, but a decrease of variable costs due to the terminated flows of materials 
between clusters.
The machines that are most convenient to duplicate are, of course, the ones most involved in flows of materials from or to machines located in other clusters.
The aim of the algorithm is to find the optimal balance between fixed and variable costs, or in other words to decide which machines to duplicate and where.

Inputs
~~~~~~~~~~~~

* From-to chart ordered by single workshops: we are evaluating the impact of the duplication of single machines inside clusters, so the change in the flow of material have
    to be evaluated by single machines and not from cluster to cluster

* Part-machine incidence matrix ordered by clusters: this time we take the composition of clusters into account to differenciate between inside-cell flows and outside-cell
flows. We only need to consider the latter.

* Cost of machines

* Matrix of the costs of single travels between machines

Outputs
~~~~~~~~~~~~

* New part-machine incidence matrix ordered by clusters, comprehensive of the duplicated machines

* New total cost of material handling




