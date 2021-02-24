Takt Time 
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Takt Time is the rate of production of a productive process and can be 
calculated for machines, workshops, assembly lines or entire plants. 
It is defined as the ratio between the available working time of the process in 
a day and the daily demand of a product/part or family of products/parts.

For example, if the working time of a machine is 960 minutes/day, and the 
product demand is 1000 pieces/day, the tackt time is 0.96 minutes/piece.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Bill of Materials: A set of raw materials and parts required to produce a 
                    finished product. 
                    Every entry reports both the type and the quantity of the 
                    materials required.

:Daily demand:  A set of values representig the daily demand [pieces/day] of 
                parts/products.

:Shifting schedulation: A set of integer values representing the shifts per day 
                        [shifts/day] for every unique workshop in the plant.

:Shift duration: The length of a shift in [hours].

:Pauses:  A set of values representing the time lost for pauses during a shift 
          [min/shift] for every unique workshop in the plant. 

:Up-time %: A set of values representing the % of time in which each machine is 
            operational. 
            Down times can occur because of machine failures or maintenance.

:PMIM:  A *n*x*m* matrix where n is the number of unique types of workshops and 
        m is the number of different parts. 

        Each element of the matrix may contain:

        - 1 if the product visits the corresponding workshop
        - 0 otherwise.

:Production cycles: A list of sequences of machinings. 
                    Every sequence is the array of machinings required to 
                    complete a part or product. Every single element of the
                    array contains a set of machining times and operator times 
                    required to process one unit of the respective product.

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Takt Times:  A *n*x*m* matrix where n is the number of unique types of 
              workshops and m is the number of different parts.
            
              - Let i be the index of unique parts, i=1,...,m
              - Let j be the index of unique workshops, j=1,...,n
            
              Each element of the matrix contains the production rate [min/pz] 
              of part i processed in workshop j.

:Workshop Takt Times: A set of values representing the production rate [min/pz] 
                      of each workshop considering the sum of the daily demands 
                      of every part processed inside it.

:Plant Takt Time: The production rate [min/pz] of the plant considering the 
                  total daily demand as a sum of the daily demands of every 
                  finished product.