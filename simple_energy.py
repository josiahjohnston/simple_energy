"""
A super-simple energy operations model. 
You may execute it with the command:
   pyomo solve --solver=glpk simple_energy.py
"""

from pyomo.environ import *

model = AbstractModel()

model.load_mwh = Param(default=2)
model.dispatch_cost = Param(default=1, doc="dispatch cost in $/MWh")

model.DispatchMWh = Var()

def Dispatch_Cost_rule(mod):
    return mod.dispatch_cost * mod.DispatchMWh
model.DispatchCost = Objective(rule=Dispatch_Cost_rule)

def Conservation_Of_Energy_rule(mod):
    return mod.load_mwh == mod.DispatchMWh
model.Conservation_Of_Energy = Constraint(rule=Conservation_Of_Energy_rule)
