# TALLLER 1 - ANALÍTICA COMPUTACIONAL 


# R {v,f} -> representa el robo
# S {v,f} -> representa el sismo
# A {v,f} -> representa la alarma
# J {v,f} -> representa la llamada de Juan
# M {v,f} -> representa la llamada de María

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

model = BayesianNetwork ([("R", "A") , ("S", "A") , ("A","J"), ("A", "M")])


cpd_r = TabularCPD ( variable ="R", variable_card =2 , values =[[0.01] ,
[0.99] ])
cpd_s = TabularCPD ( variable ="S", variable_card =2 , values =[[0.02] ,
[0.98] ])

cpd_a = TabularCPD (
variable ="A",
variable_card =2 ,
values =[
[0.95,0.94,0.29,0.001],
[0.05,0.06,0.71,0.999],
],
evidence =["R", "S"] ,
evidence_card =[2 , 2] ,
)

cpd_j = TabularCPD (
variable ="J",
variable_card =2 ,
values =[
[0.9,0.05],
[0.1,0.95],    
],
evidence =["A"] ,
evidence_card =[2] ,
)


cpd_m = TabularCPD (
variable ="M",
variable_card =2 ,
values =[
[0.7,0.01],
[0.3,0.99],    
],
evidence =["A"] ,
evidence_card =[2] ,
)

model.add_cpds(cpd_r , cpd_s , cpd_a ,cpd_j,cpd_m )

model.check_model()


from pgmpy.inference import VariableElimination
infer = VariableElimination (model)

print ( model . get_independencies () )

