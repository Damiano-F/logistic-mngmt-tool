Formation of the clusters
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the similarity matrix is set, we can proceed transforming it by 
sequentially grouping the workshops together, starting from the ones with the 
highest similarity values, until every workshop joins the same cluster.

As the process goes on, more workshops with lower similarity value join the 
same cluster, so the overall similarity value of the clusters decrease with 
every grouping operation.

The algorithms used to perform this operation are C-LINK, D-LINK, UPGMA and 
Galan.
When the process is concluded, the user can select a lower boud to the 
similarity value: the clusters generated with a similarity value below the one 
desired by the user are excluded from the optimal solution.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Similarity matrix: An *n* x *n* matrix  where *n* is the number of unique types 
                    of workshops. 
                    Each element contains a value between 0 and 1 representing 
                    the estimate of the similarity between two different 
                    workshops.

:Daily demand:  A set of values representig the daily demand [pieces/day] of 
                parts/products.

:Lower similarity bound:    A value between 0 and 1 which limits the number of
                            aggregations.

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Clusters of workshops: A set of clusters. Each cluster contains a set of
                        workshops.

:Clustered PMIM:    A *n* x *m* matrix where *n* is the number of unique types of 
                    workshops and *m* is the number of different parts. 

                    Each element of the matrix may contain:

                    - 1 if the product visits the corresponding workshop
                    - 0 otherwise.

                    The *n* workshops have been reordered according to the sets
                    of clusters.

:Dendrogram: A tree-like diagram which represents the clustering process.