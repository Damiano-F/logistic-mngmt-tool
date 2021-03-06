

class ProductionPhase:

    def __init__(self, partID, phaseID, workshopID, machTiming, opTiming, 
                    placingTiming, nPlacings, setupTiming)

        self.partID= partID
        self.phaseID= phaseID
        self.workshopID= workshopID
        self.machTiming= machTiming
        self.opTiming= opTiming
        self.placingTiming= placingTiming
        self.nPlacings= nPlacings
        self.setupTiming= setupTiming



class ProductionCycle:

    # phases is a list of ProductionPhase objects, ordered by phaseID
    def __init__(self, partID, phases)

        self.partID= partID
        self.phases= phases



class Part:

    # id is partID 
    def __init__(self, id, cycles, bom, demand, per_pallet):

        self.id= id
        self.cycle= cycle
        self.bom= bom
        self.demand= demand
        self.per_pallet= per_pallet

    # get methods (not for now)

    # set method for demand
    def setDemand(self, demand):

        self.demand= demand
        
