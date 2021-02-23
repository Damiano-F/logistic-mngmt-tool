Block Layout Formation
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To decide how to place the clusters in the layout of the manufacturing plant, 
the first step is to assign a priority to each cluster, based on the amount of 
materials flowing from and to them.
The fist clusters to be placed will be the ones with the highest material flow, 
so that we can be sure to place them close to each other.
On the contrary, clusters with low material flows can be assigned to the 
periphery of the plant layout, so they will enter last.

The algorithms implemented in this step are Punctual Flow, Total Flow and 
Weighted Flow.
In general, they will present different solutions to the user. 
Those solutions can be compared only in terms of costs, or the user can decide 
to accept a solution rather than another one because of various considerations 
about the effective dislocation of the spaces in the layout or the presence of 
qualitative relations between clusters, for example in terms of safety
(placing a cluster in which hot material is processed next to a cluster that 
processes flammable material can be dangerous).
In general, the user should be able to add personalized boundaries to the 
optimization models, depending from case to case.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:From-to chart: see from-to chart documentation

:Qualitative relations matrix:  similar to the similarity matrix, it represents 
                                the qualitative relations between clusters (or 
                                workshops) for what regards qualitative 
                                characteristics like safety, communication 
                                needs with other clusters etc.

.. TO DEFINE!!

Other custom boundaries about clusters positions 


Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Clusters insertion order:  Clusters insertion order in the layout