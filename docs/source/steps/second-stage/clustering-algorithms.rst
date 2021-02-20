Formation of the clusters
------------------------------

Context
~~~~~~~~~~~~

Once the similarity matrix is set, we can proceed transforming it by sequentially grouping the workshops together, starting from the ones with the highest similarity 
values, until every workshop joins the same cluster. As the process goes on, more workshops with lower similarity value join the same cluster, so the overall similarity
value of the clusters decrease with every grouping operation. The algorithms used to perform this operation are C-LINK, D-LINK, UPGMA and Galan.
When the process is concluded, the user can select a lower boud to the similarity value: the clusters generated with a similarity value below the one desired by the user 
are excluded from the optimal solution.

Inputs
~~~~~~~~~~~~

* Similarity matrix

* Daily demand of products/parts

* Lower similarity bound

Outputs
~~~~~~~~~~~~

* Clusters of workshops

* Part-machine incidence matrix ordered by clusters

* Dendrogram: tree-like diagram of the aggregation series