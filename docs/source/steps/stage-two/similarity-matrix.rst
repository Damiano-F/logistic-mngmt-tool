Creation of the Similarity Matrix
--------------------------------------------------------------------------------

Context
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To optimize the flow of materials in a plant, it's convenient to group together 
machines visited by the same products.  
Additional characteristics may be taken into account, like the quantity of 
parts processed and the processing times. 
The result of the grouping process is a set of cells, each one dedicated to the 
production of a family of similar products. 
There are different approaches for the evaluation of the similarity between 
different machines, but the end result is always the similarity matrix.

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:PMIM:  A *n* x *m* matrix where *n* is the number of unique types of workshops 
        and *m* is the number of different parts. 

        Each element of the matrix may contain:

        - 1 if the product visits the corresponding workshop
        - 0 otherwise.

:Daily demand:  A set of values representig the daily demand [pieces/day] of 
                parts/products.

:Production cycles: A list of sequences of machinings. Every sequence is the 
                    array of machinings required to complete a part or product. 
                    Every single element of the array contains a set of 
                    machining times and operator times required to process one 
                    unit of the respective product.

..note::    The role of the setup times in the evaluation of similarity indexes
            is to be clarified.

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Similarity matrix: An *n* x *n* matrix where *n* is the number of unique types 
                    of workshops. 
                    Each element contains a value between 0 and 1 representing 
                    the estimate of the similarity between two different 
                    workshops.
