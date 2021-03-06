Joint Economic Lot Size Calculator
--------------------------------------------------------------------------------

Purpose
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To find the optimal (in terms of costs) lot size and the optimal shipping 
routine (in terms of number of shipment and quantity of products shipped).

Inputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Setup cost Csu:

    *   Measure unit: [€/setup]
    *   Domain: R>= 0
    *   Description: with every change from the production of a product or 
        family of products to another, it is usually necessary for the vendor 
        to carry out some operations on the machines to enable them to process 
        the raw materials in the right way.

:Procurement operations cost Cpo:

    *   Measure unit: [€/order]
    *   Domain: R>= 0
    *   Description: for every new lot order, the buyer incurs in costs for the 
        activation of the procurement office.

:Vendor storage cost Csv:

    *   Measure unit: [€/(Pz*year)]
    *   Domain: R>= 0
    *   Description: for every stored product, the vendor incurs in costs due to 
        material handling, warehouse maintainance etc.

:Buyer storage cost Csb:

    *   Measure unit: [€/(Pz*year)]
    *   Domain: R>= 0
    *   Description: for every stored product, the buyer incurs in costs due to 
        material handling, warehouse maintainance etc.

:Production rate P:

    *   Measure unit: [Pz/year]
    *   Domain: N>0
    *   Description: number of units produced by the vendor in an year.

:Consumption rate D:

    *   Measure unit: [Pz/year]
    *   Domain: N>0
    *   Description: number of units consumed by the buyer in an year.

:Number of shipments n:

     *  Measure unit: [shipments/lot]
     *  Domain: N>0
     *  Description: number of shipments to transfer the whole quantity of 
        products of one lot from vendor to Buyer. Inizialized at n=1.

:Shipment quantity growth rate I:

    *   Domain: I ∈ R, 1<= I <=P/D
    *   Description: rate of increase in the quantity of products shippents 
        from one shipment to the next one. Initialized at G=1.

Outputs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

:Optimal shipments number Nopt:

    *   Measure unit: [shipments/lot]
    *   Domain: N>0
    *   Description: optimal number of shipments to transfer the whole quantity 
        of products of one lot from vendor to Buyer.

:Optimal shipment quantity growth rate Iopt:

    *   Domain: I ∈ R, 1<= I <=P/D
    *   Description: optimal rate of increase in the quantity of products 
        shippents from one shipment to the next one.

:Quantity of products shipped for every shipment q1,...,qn:

    *   Domain: array of n values ∈ N>0

:Quantity of products shipped to complete one lot Qopt:

    *   Measure unit: [Pz/lot]
    *   Domain: N>0
    *   Description: optimal lot size.

:Optimal lot management cost Copt:

    *   Measure unit: [Pz/year]
    *   Domain: R>0

:Top and average vendor storage Gmax, Gavg:

    *   Domain: N>0

:Top and average vendor storage Gmax, Gavg:

    *   Domain: N>0

:Storage graphics over time for vendor and buyer
