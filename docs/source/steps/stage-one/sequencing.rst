Sequencing 
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To avoid the risk of overproduction, it's a good practice to produce every 
product in lots as small as possible and invest more time in setups. The 
sequencing algorithm divides the daily production in sequences. 
At the start of every sequence, operators have to stop the production and spend 
some time for the setup. 
The algorithm fits the maximum number of sequences in a day, considering that 
the total setup time have to be small enought to allow the completion of the 
daily production.
For example, if every setup is 1 hour and the number of sequences per day is 10, 
the machines will be in down time for 10 hours a day. Will it be too much to 
complete the daily production?

Inside a single sequence, there will be a serie of different parts. The good 
practices of lean production state that the production in batches should be
avoided, and every single product should be as distant as possible from the next 
product of the same kind in the sequence. This process is called sequencing.

For example, given products A, B and C, produced 3 times each in one sequence, 
the optimal sequencing is ABCABCABC instead of AAABBBCCC.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Production cycles: A list of sequences of machinings. 
                    Every sequence is the array of machinings required to 
                    complete a part or product. 
                    Every single element of the array contains the setup time 
                    required to start the production of that product.

:Daily demand:  A set of values representig the daily demand [pieces/day] of 
                parts/products.

:Shifting schedulation: A set of integer values representing the shifts per day 
                        [shifts/day] for every unique workshop in the plant.

:Shift duration: The length of a shift in [hours].

:Pauses:    A set of values representing the time lost for pauses during a 
            shift [min/shift] for every unique workshop in the plant. 

:Up-time %: A set of values representing the % of time in which each machine is 
            operational. Down times can occur because of machine failures or 
            maintenance.

:Number of machines per workshop:   A set of integers representing the number 
                                    of machines present in every workshop.

:Total workshops machining times:   A set of values [min/day] representing, for 
                                    each workshop, the sum of all the machinig 
                                    times over one day.

:Takt Times:    A *n*x*m* matrix where n is the number of unique types of 
                workshops and m is the number of different parts.
            
                - Let i be the index of unique parts, i=1,...,m
                - Let j be the index of unique workshops, j=1,...,n
            
                Each element of the matrix contains the production rate [min/pz] 
                of part i processed in workshop j.

:Workshop Takt Times:   A set of values representing the production rate 
                        [min/pz] of each workshop considering the sum of the 
                        daily demands of every part processed inside it.

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Sequence Count:    A set of integers showing, for each workshop, how many times 
                    the sequence is repeated over a day.

:Sequence order:    A set associating a list for each workshop. 
                    Every list shows the order in which each product is 
                    processed during one sequence.

