"""
A super-simple energy operations model. 
You may execute it with the command:
   python simple_energy.py
"""

from pyomo.environ import *

# Start by creating a model object. Store it in a variable named "model" if
# you want to work with the pyomo or pysp command-line tools. Model components
# are added next.
energy_model = AbstractModel()

# Define parameters along with default values so we don't have to use a 
# separate data file.
energy_model.load_mwh = Param(default=2)
energy_model.dispatch_cost = Param(default=1, doc="dispatch cost in $/MWh")

# Decision variables
energy_model.DispatchMWh = Var()

# The objective is written in two steps: 
# 1: A python function that takes a model as an argument at run time, and returns
# a mathematical formula using components from the model.
# 2: Attach the python function to the model as the objective.
def Dispatch_Cost_rule(mod):
    return mod.dispatch_cost * mod.DispatchMWh
energy_model.DispatchCost = Objective(rule=Dispatch_Cost_rule)

# The constraint is also written in two steps, and needs to return
# either an equality or inequality relationship.
def Conservation_Of_Energy_rule(mod):
    return mod.load_mwh == mod.DispatchMWh
energy_model.Conservation_Of_Energy = Constraint(rule=Conservation_Of_Energy_rule)


# Some boilerplate code to execute this model with `python simple_energy.py`
if __name__ == '__main__':
    from pyomo.opt import SolverFactory
    import pyomo.environ
    opt = SolverFactory("glpk")
    model_instance = energy_model.create_instance()
    results = opt.solve(model_instance)
    model_instance.pprint()
    results.write()    
