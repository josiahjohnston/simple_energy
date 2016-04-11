"""
A super-simple energy operations model. 
You may execute it with the command:
   python simple_energy.py
"""

from pyomo.environ import *

# Start by creating a model object. Store it in a variable named "model" if
# you want to work with the pyomo or pysp command-line tools. Model components
# are added next.
model = AbstractModel()

# A set of timepoints to dispatch across. Sets are written in ALL_CAPS_WITH_UNDERSCORES
# These will be indexes to some parameters, variables and constraints, so I'll
# define them at the top. 
# Their labels can be anything I want: a word, timestamp or whatever.
model.TIMEPOINTS = Set(initialize=['peak', 'mean'])

# Define parameters along with default values so we don't have to use a 
# separate data file.
model.timepoint_duration_hr = Param(model.TIMEPOINTS, default={'peak': 10, 'mean':8750})
model.load_mw = Param(model.TIMEPOINTS, default={'peak': 4, 'mean':2})
model.dispatch_cost = Param(model.TIMEPOINTS, default=1, doc="dispatch cost in $/MWh")

# Decision variables
model.DispatchMW = Var(model.TIMEPOINTS)

# The objective is written in two steps: 
# 1: A python function that takes a model as an argument at run time, and returns
# a mathematical formula using components from the model.
# 2: Attach the python function to the model as the objective.
def Dispatch_Cost_rule(mod):
    return sum(
        mod.dispatch_cost[t] * mod.DispatchMW[t] * mod.timepoint_duration_hr[t]
        for t in mod.TIMEPOINTS)
model.DispatchCost = Objective(rule=Dispatch_Cost_rule)

# The constraint is also written in two steps, and needs to return
# either an equality or inequality relationship.
def Conservation_Of_Energy_rule(mod, t):
    return mod.load_mw[t] == mod.DispatchMW[t]
model.Conservation_Of_Energy = Constraint(model.TIMEPOINTS, rule=Conservation_Of_Energy_rule)


# Some boilerplate code to execute this model with `python simple_energy.py`
if __name__ == '__main__':
    from pyomo.opt import SolverFactory
    import pyomo.environ
    opt = SolverFactory("glpk")
    model_instance = model.create_instance()
    results = opt.solve(model_instance)
    model_instance.pprint()
    results.write()    
