Machines Estimate
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To manage the flow of a certain quantity of materials trough the plant, there 
needs to be enough processing power available. 
It is possible to calculate the number of machines needed in every workshop as a
ratio between the total processing time for a day of production and the working 
time available to a single machine in a day.

For example, with 9600 minutes of processing/day and 960 minutes of work/day, 
the workshop will need exactly 10 machines. 

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Production cycles: A list of sequences of machinings. Every sequence is the 
                    array of machinings required to complete a part or product. 
                    Every single element of the array contains a set of 
                    machining times and operator times required to process one 
                    unit of the respective product.

:Daily demand:  A set of values representig the daily demand [pieces/day] of 
                parts/products.

:Bill of Materials: A set of raw materials and parts required to produce a 
                    finished product. 
                    Every entry reports both the type and the quantity of the 
                    materials required.

:PMIM:  A *n*x*m* matrix where *n* is the number of unique types of workshops 
        and *m* is the number of different parts. 

        Each element of the matrix may contain:

        - 1 if the product visits the corresponding workshop
        - 0 otherwise.

:Shifting schedulation: A set of integer values representing the shifts per day 
                        [shifts/day] for every unique workshop in the plant.

:Shift duration: The length of a shift in [hours].

:Pauses:    A set of values representing the time lost for pauses during a shift 
            [min/shift] for every unique workshop in the plant. 

:Up-time %: A set of values representing the % of time in which each machine is 
            operational. 
            Down times can occur because of machine failures or maintenance.

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Number of machines per workshop:   A set of integers representing the number 
                                    of machines present in each workshop.

:Total workshops machining times:   A set of values [min/day] representing, for 
                                    each workshop, the sum of all the machinig 
                                    times over one day.
