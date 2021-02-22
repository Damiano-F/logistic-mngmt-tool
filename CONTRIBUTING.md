## Contributing to the project



## Documentation rules

The documentation is build with Sphinx.

### Documentation mantra:

Documentation is part of the software.

Software is alive and, as such, documentation is bound to change at some point.

Everyone makes errors and it's ok.

What it's not ok is pushing build breaking changes (if it can be prevent):
Compile the docs and check if your changes have been compiled correctly before
pushing.

Do not compound information in a single sentence. Break it down.

Simple and concise sentences make it easier to read and understand.

Tables, grids, graphs and diagrams are your friend.

The first draft is almost never the best possible.

Every line of text of the documentation must not exceed 80 characters.
Every line of code must not exceed 120 characters.

### ReStructured Text cheatsheet:

```

Chapters are define as a single TOCs in index.rst

The following lines must be at least as long as the title right above them.

Section:        

================================================================================

Subsection:     

--------------------------------------------------------------------------------

Subsubsection:  

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Paragraph:      

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

:field-definition:

.. note:: Blue note ticket

.. warning::    Yellow note ticket - used for making sure the reader catch an
                important piece of information.



```
