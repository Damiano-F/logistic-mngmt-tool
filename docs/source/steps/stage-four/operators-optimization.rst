Operators Optimization
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One of the main advantages of a layout organized by clusters is that a single 
operator can control more different machines, allowing a reduction of the total 
number of operators needed. 
With the clusters formation process concluded, it is possible to evaluate the 
number of operators assigned to every cell as the ratio between the total time 
of working required to complete the daily production, and the disposable time 
of every operator, which depends from the organization of the shifts.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Part-machine incidence matrix by clusters

* Production cycles with informations about the working time of every operation

* Takt time (rate of production) of the families of products assigned to clusters

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Number of operators assigned to every cluster