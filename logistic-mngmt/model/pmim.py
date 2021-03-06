import pandas as pd
from iteration_utilities import unique_everseen, duplicates
from itertools import chain


class pmim (pd.DataFrame):

# rows are a list of workshops, columns are a list of products
    def __init__(self, parts):

        # returns a list of unique parts IDs and a list of multiple parts IDs
        partsID= []
        for i in parts:
            partsID.append(i.id)

        unique_partsID= list(unique_everseen(partsID))
        return print("List of unique parts: ", unique_partsID)

        multiples= list(unique_everseen(duplicates(partsID)))
        return print("List of multiple parts: ", multiples)

        if len(multiples)!=0:
            raise Exception("Part IDs must be unique. Check imput data for parts sharing same ID")


        # iterate trough parts and inside cycles

        # list of unique workshops
        workshops= []
        for i in parts:
            cycle= i.cycle
            workshops= list(chain(workshops, cycle))

        unique_workshops= list(unique_everseen(workshops))

        return print("List of unique workshops: ", workshops)

        # list of ProductionCycle obj for each part
        parts_cycles= []
        for i in parts:
            parts_cycles.append(i.cycle)

        # list of ProductionPhase obj for each cycle
        cycles_phases= []
        for i in parts_cycles:
            cycles_phases.append(i.phases)

        # list of workshops for each cycle, without timings etc.
        workshops_phases= []
        for i in cycles_phases:
            lst= []
            for j in i:
                lst.append(j.workshopID)
            workshops_phases.append(lst)

        # list of unique workshops for each cycle
        unique_workshops_phases= []
        for i in workshops_phases:
            unique_workshops_phases.append(list(unique_everseen(i)))

        # list of PMIM columns
        columns= []
        for i in unique_workshops_phases:
            lst= []
            for j in unique_workshops:
                n= i.count(j)
                lst.append(n)
            columns.append(lst)

        # creation of PMIM column labels
        keys= ["Null"]
        for i in parts:
            keys.append(i.id)

        # creation of PMIM row labels
        values= []
        values.append(unique_workshops)
        for i in columns:
            values.append(i)

        # creation of PMIM dictionary
        pmim_dict= dict(zip(keys, values))

        # creation of PMIM dataframe
        pmim= pd.DataFrame.from_dict(pmim_dict)

        return pmim



