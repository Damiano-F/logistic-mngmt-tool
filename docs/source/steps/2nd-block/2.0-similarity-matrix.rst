Creation of the Similarity Matrix
------------------------------------

Context
~~~~~~~~~~~~

To optimize the flow of materials in a plant, it's convenient to group machines that share the processing of the same products as well as other characteristics, like the
quantity of parts processed and the processing times, inside cells dedicated to the production of a serie of similar products. 
There are a serie of indexes that allow us to evaluate the similarity of different machines, but the end result is always the similarity matrix: a square structure wich 
shows a list of workshops both in the rows and in the columns. The elements of the matrix are adimensional real numbers from 0, if a couple of workshops is not similar, 
to 1 when a couple of workshops is perfectly similar.
For example, the diagonal of the matrix is filled with "1" because the similarity value between a workshop and itself is always perfect.

The similarity matrix is built starting from the part-machine incidence matrix and applying a variety of linear functions to it.

Inputs
~~~~~~~~~~~~

* Part-machine incidence matrix: see PMIM in the documentation

* Daily demand of parts/products

* Production cycles: for every product or part, the sequence of workshops visited and informations about the machining process, like the processing times

Outputs
~~~~~~~~~~~~

* Similarity matrix
