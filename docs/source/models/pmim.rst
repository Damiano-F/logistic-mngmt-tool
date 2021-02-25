Part-Machine Incidence Matrix 
--------------------------------------------------------------------------------

Definition:

:PMIM:  A *n*x*m* matrix where *n* is the number of unique types of workshops 
        and *m* is the number of different parts. 

        Each element of the matrix may contain:

        - 1 if the product visits the corresponding workshop
        - 0 otherwise.

PMIM behaves like a pandas.DataFrame where columns labels refer to parts and
rows labes refer to workshops. 

Used in steps: 

-   Evaluation of Machines Duplication Options
-   Operators Optimization
-   Machines Estimate
-   Operators Assignment
-   Takt Time 
-   Formation of the clusters
-   Assignment of products/parts to clusters
-   Creation of the Similarity Matrix

The requirements are:

-   PMIM must be diagonalizable
-   PMIM must be expansable
-   Columns and rows of PMIM must be permutable by parts or machines
