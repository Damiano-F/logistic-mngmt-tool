Operators Optimization
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One of the main advantages of a layout organized by clusters is that a single 
operator can control more different machines, allowing a reduction of the number 
of operators needed. 
With the clustering process concluded, it is possible to evaluate the number of 
operators assigned to every cell.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:New diagonalized PMIM: A *n*x*m* matrix where *n* is the number of unique types 
                        of workshops and *m* is the number of different parts. 

                        Each element of the matrix may contain:

                        - 1 if the product visits the corresponding workshop
                        - 0 otherwise.

                        The *n* workshops have been reordered according to the 
                        sets of new clusters.
                        The *m* parts have been reordered according to parts 
                        assignment.

:Production cycles: A list of sequences of machinings. Every sequence is the 
                    array of machinings required to complete a part or product. 
                    Every single element of the array contains a set of 
                    machining times and operator times required to process one 
                    unit of the respective product.

:Takt Times:  A *n*x*m* matrix where *n* is the number of unique types of 
              clusters and *m* is the number of different parts.
            
              Let i be the index of unique parts, i=1,...,m
              Let j be the index of unique clusters, j=1,...,n
            
              Each element of the matrix contains the production rate [min/pz] 
              of part i processed in cluster j.

:Workshop Takt Times: A set of values representing the production rate [min/pz] 
                      of each cluster considering the sum of the daily demands 
                      of every part processed inside it.

:Plant Takt Time: The production rate [min/pz] of the plant considering the 
                  total daily demand as a sum of the daily demands of every 
                  finished product.

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Number of operators per cluster:   A set of integers associating to each 
                                    cluster the number of operators required.