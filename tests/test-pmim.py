from logistic-mngmt.model import Pmim, Part, ProductionCycle, ProductionPhase

# all the phases
pp1=    ProductionPhase("30", "w4", 0, 0, 0, 0, 0) 
pp2=    ProductionPhase("20", "w3", 0, 0, 0, 0, 0) 
pp3=    ProductionPhase("50", "w1", 0, 0, 0, 0, 0) 
pp4=    ProductionPhase("10", "w2", 0, 0, 0, 0, 0) 
pp5=    ProductionPhase("40", "w3", 0, 0, 0, 0, 0) 
pp6=    ProductionPhase("10", "w2", 0, 0, 0, 0, 0) 
pp7=    ProductionPhase("30", "w2", 0, 0, 0, 0, 0) 
pp8=    ProductionPhase("10", "w4", 0, 0, 0, 0, 0) 
pp9=    ProductionPhase("20", "w1", 0, 0, 0, 0, 0) 
pp10=   ProductionPhase("40", "w3", 0, 0, 0, 0, 0) 
pp11=   ProductionPhase("30", "w1", 0, 0, 0, 0, 0) 
pp12=   ProductionPhase("10", "w4", 0, 0, 0, 0, 0) 
pp13=   ProductionPhase("10", "w2", 0, 0, 0, 0, 0)
pp14=   ProductionPhase("20", "w1", 0, 0, 0, 0, 0) 
pp15=   ProductionPhase("20", "w2", 0, 0, 0, 0, 0) 
pp16=   ProductionPhase("30", "w3", 0, 0, 0, 0, 0) 
pp17=   ProductionPhase("20", "w4", 0, 0, 0, 0, 0)

# equivalent of production cycles
phases_lst_p1= [pp4, pp2, pp1]
phases_lst_p2= [pp6, pp9, pp7, pp5, pp3]
phases_lst_p3= [pp8, pp14, pp11, pp10]
phases_lst_p4= [pp12, pp15, pp16]
phases_lst_p5= [pp13, pp17]

# production cycles per product
pc1= ProductionCycle(phases_lst_p1)
pc2= ProductionCycle(phases_lst_p2)
pc3= ProductionCycle(phases_lst_p3)
pc4= ProductionCycle(phases_lst_p4)
pc5= ProductionCycle(phases_lst_p5)

# parts
p1= Part("01", pc1, "null", 0, 0)
p2= Part("02", pc2, "null", 0, 0)
p3= Part("03", pc3, "null", 0, 0)
p4= Part("04", pc4, "null", 0, 0)
p5= Part("05", pc5, "null", 0, 0)

# list of parts
parts= [p1, p2, p3, p4, p5]

pmim= Pmim(parts)

print(pmim)





