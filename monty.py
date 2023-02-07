# Taller 1 - ANALÍTICA COMPUTACIONAL 

# Definición de las variables aleatorias

# U -> puerta seleccionada por el usuario  
# C -> puerta donde está el carro
# A -> puerta que abre el animador

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

model = BayesianNetwork ([("U", "A") , ("C", "A") ])

cpd_c = TabularCPD ( variable ="C", variable_card =3 , values =[[0.33] ,[0.33] , [0.33]])

cpd_u = TabularCPD ( variable ="U", variable_card =3 , values =[[0.33] ,[0.33] , [0.33]])

cpd_a = TabularCPD (variable ="A", variable_card =3 , values =[
    [0 , 0 , 0 , 0 , 0.5 , 1 , 0 , 1 , 0.5] ,
    [0.5 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0.5] ,
    [0.5 , 1 , 0 , 1 , 0.5 , 0 , 0 , 0 , 0] ,
    ] ,
    evidence =["C", "U"] ,
    evidence_card =[3 , 3] ,)

model.add_cpds (cpd_c , cpd_u , cpd_a)

model.check_model ()

from pgmpy . inference import VariableElimination
infer = VariableElimination (model)

posterior_p = infer.query (["C"] , evidence ={"U": 0 , "A": 2})

print(posterior_p)
