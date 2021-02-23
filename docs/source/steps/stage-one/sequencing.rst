Sequencing 
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To avoid the risk of overproduction, it's a good practice to produce every 
product in lots as small as possible and choose to invest more time in setups.

The sequencing algorithm divides the daily production in sequences and every 
sequence has its own setup time. It then fits the maximum number of sequences 
in a day, considering that the total setup time can't be greater than the free 
time left from the processing time (a machine can't work while it's undergoing 
the setup).

For example, if every setup is 1 hour and the number of sequences per day is 10, 
the machines will be in down time for 10 hours a day. Will it be too much to 
complete the daily production?

Inside a single sequence, there will be a serie of different products or parts. 

The good practice of lean production states that the production in batches 
should be avoided, and every single product should be as distant as possible 
from the nex product of the same kind in the sequence. This process is called 
sequencing.

For example, given products A, B and C, produced 3 times each in one sequence, 
the correct sequencing is ABCABCABC instead of AAABBBCCC.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Production cycles: Production cycles for every product or part, the sequence 
                    of workshops visited and informations about the machining 
                    process, like the processing times.

:Daily demand:  The daily demand of every parts/products for the process 
                considered.

:Working time:  The available Working time in a day for every workshop, 
                considering also pauses and machine downtimes, usually in 
                minutes/day.

:Machine count: Number of machines in the workshop considered.

:Total machining time:  The total machining time over one day.

:Takt timings:  Takt timing for every process in the plant, both considering 
                the total of the daily production and separately for each 
                product/part.

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Sequence Count: Number of sequences

:Sequence order: Sequencing of the sequence

