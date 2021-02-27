Similarity Matrix
--------------------------------------------------------------------------------

An *n* x *n* matrix where *n* is the number of unique types of workshops. 
Each element contains a value between 0 and 1 representing the estimate of the 
similarity between two different workshops.

Constructor:

Created in step "Creation of the Similarity Matrix".

Properties:

-   Set of similarity values for every couple of workshops [local, variable]

Use Cases:

-   Formation of the clusters

Requirements:

-   Must be mutable
-   Must be permutable
-   Must be possible to change dimension of the matrix