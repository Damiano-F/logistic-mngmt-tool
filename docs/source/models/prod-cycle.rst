Production cycle
--------------------------------------------------------------------------------

Definition:

Ordered sequence of couples of workshops and production timings.

Properties:

- Associated to a unique part [local, constant]

Use Cases:

-   Operators Optimization
-   Machines Estimate
-   Operators Assignment
-   PMIM Formation
-   Sequencing
-   Takt Time 
-   From-to Chart Formation
-   Assignment of products/parts to clusters
-   Creation of the Similarity Matrix

Requirements:

-   Must be unmutable

Production phase
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Definition:

A single step in the production cycle of a material part. 

Properties:

-   ID [local, constant]
-   machining timings [local, constant]
-   operator timings [local, constant]
-   setup timing [local, constant]
-   placing timings [local, constant]

Use Cases:

-   Operators Optimization
-   Machines Estimate
-   Operators Assignment
-   PMIM Formation
-   Sequencing
-   Takt Time 
-   From-to Chart Formation
-   Assignment of products/parts to clusters
-   Creation of the Similarity Matrix

Requirements:

-   Must be unmutable