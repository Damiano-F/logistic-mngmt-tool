Material Part
--------------------------------------------------------------------------------

Synonim: Product.

Definition: 

Subtypes:

-   Final product
-   Composite part
-   Raw material part

Constructor:

Requires ...

Properties:

-   :Name: [local, constant]
-   ID
-   Production cycle
-   Bill of Materials
-   Daily demand
-   Pieces per pallet

Use Cases:

-   Operators Optimization
-   Machines Estimate
-   Operators Assignment
-   PMIM Formation
-   Sequencing
-   Takt Time 
-   From-to Chart Formation
-   Formation of the clusters
-   Assignment of products/parts to clusters
-   Creation of the Similarity Matrix

Requirements:

-    Every part must have an unique ID

Bill of Materials
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Description:

Constructor:

Imput data can come in different formats.

Properties:

-   One list for each composite part
-   Each list reports the required parts and theirs respective quantities in 
    order to assemble a single composite part