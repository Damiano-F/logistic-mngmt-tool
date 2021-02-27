From-To-Chart Matrix
--------------------------------------------------------------------------------

An *n*x*n* matrix where *n* is the number of unique types of workshops or 
clusters. 
Each element contains an integer representing the inbound or outbound flows 
[travels/day] between a workshop or cluster and all the other ones.

Constructor:

Created in the step "From-To Chart Formation"

Properties:

-   Cell elements [travels/day] [local, variable]

Use Cases:

-   Block Layout Formation
-   Evaluation of Machines Duplication Options
-   Cost of Material Handling 

Requirements:

-   Must be permutable
-   Must be mutable
