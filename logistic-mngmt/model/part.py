

class ProductionPhase:

    # cancelled partID
    def __init__(self, phaseID, workshopID, machTiming, opTiming, 
                    placingTiming, nPlacings, setupTiming)

        self.phaseID= phaseID
        self.workshopID= workshopID
        self.machTiming= machTiming
        self.opTiming= opTiming
        self.placingTiming= placingTiming
        self.nPlacings= nPlacings
        self.setupTiming= setupTiming



class ProductionCycle:

    # phases is a list of ProductionPhase objects, ordered by phaseID
    def __init__(self, phases)

        self.phases= phases
        self.__partID= "unidentified"

    @property
    def partID(self):
        return self.__partID

    @partID.setter
    def partID(self, partID):
        self.__partID= partID

class Part:

    # id is partID 
    def __init__(self, id, cycle, bom, demand, per_pallet):

        self.id= id
        self.cycle= cycle
        self.cycle.partID= id
        self.bom= bom
        self.demand= demand
        self.per_pallet= per_pallet

    # get methods (not for now)

    # set method for demand
    def setDemand(self, demand):

        self.demand= demand
        
