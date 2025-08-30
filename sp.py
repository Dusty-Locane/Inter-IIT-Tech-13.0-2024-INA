import pandas as pd
from pulp import LpMinimize, LpProblem, LpVariable, lpSum

# Sample Data
plants = ['Plant1', 'Plant2']
distribution_centers = ['DC1', 'DC2']
customers = ['Customer1', 'Customer2']

# Cost and Demand Data (You can replace these with actual data inputs)
production_costs = {'Plant1': 10, 'Plant2': 12}  # Cost per unit at each plant
transport_cost_plant_to_dc = {('Plant1', 'DC1'): 2, ('Plant1', 'DC2'): 4,
                              ('Plant2', 'DC1'): 3, ('Plant2', 'DC2'): 1}  # Transport cost per unit
transport_cost_dc_to_customer = {('DC1', 'Customer1'): 5, ('DC1', 'Customer2'): 6,
                                 ('DC2', 'Customer1'): 4, ('DC2', 'Customer2'): 3}  # Transport cost per unit
handling_cost_dc = {'DC1': 1, 'DC2': 1.5}  # Handling cost per unit at each DC

plant_capacity = {'Plant1': 1000, 'Plant2': 800}  # Capacity in units
dc_capacity = {'DC1': 1200, 'DC2': 1000}  # Capacity in units
customer_demand = {'Customer1': 600, 'Customer2': 500}  # Demand in units

# Initialize the Optimization Problem
problem = LpProblem("E2E_Network_Optimization", LpMinimize)

# Decision Variables
# Variables for flow of goods from Plants to DCs
flow_plant_to_dc = LpVariable.dicts("Flow_Plant_to_DC",
                                    [(p, d) for p in plants for d in distribution_centers],
                                    lowBound=0, cat="Continuous")

# Variables for flow of goods from DCs to Customers
flow_dc_to_customer = LpVariable.dicts("Flow_DC_to_Customer",
                                       [(d, c) for d in distribution_centers for c in customers],
                                       lowBound=0, cat="Continuous")

# Objective Function: Minimize Total Cost (Production + Transportation + Handling)
problem += lpSum([production_costs[p] * flow_plant_to_dc[(p, d)]
                  for p in plants for d in distribution_centers]) + \
           lpSum([transport_cost_plant_to_dc[(p, d)] * flow_plant_to_dc[(p, d)]
                  for p in plants for d in distribution_centers]) + \
           lpSum([handling_cost_dc[d] * flow_dc_to_customer[(d, c)]
                  for d in distribution_centers for c in customers]) + \
           lpSum([transport_cost_dc_to_customer[(d, c)] * flow_dc_to_customer[(d, c)]
                  for d in distribution_centers for c in customers])

# Constraints
# 1. Supply constraint: Plant production cannot exceed its capacity
for p in plants:
    problem += lpSum([flow_plant_to_dc[(p, d)] for d in distribution_centers]) <= plant_capacity[p], f"Plant_Capacity_{p}"

# 2. Demand constraint: Customer demand must be met
for c in customers:
    problem += lpSum([flow_dc_to_customer[(d, c)] for d in distribution_centers]) >= customer_demand[c], f"Customer_Demand_{c}"

# 3. Distribution Center capacity constraint
for d in distribution_centers:
    problem += lpSum([flow_plant_to_dc[(p, d)] for p in plants]) <= dc_capacity[d], f"DC_Capacity_{d}"

# 4. Flow balance constraint at DCs: inflow to DC equals outflow to customers
for d in distribution_centers:
    problem += lpSum([flow_plant_to_dc[(p, d)] for p in plants]) == \
               lpSum([flow_dc_to_customer[(d, c)] for c in customers]), f"Flow_Balance_{d}"

# Solve the problem
problem.solve()

# Output Results
print("Optimization Status:", problem.status)
print("Optimal Total Cost:", problem.objective.value())

# Display results for flows from Plants to DCs
for (p, d) in flow_plant_to_dc:
    print(f"Flow from {p} to {d}: {flow_plant_to_dc[(p, d)].value()} units")

# Display results for flows from DCs to Customers
for (d, c) in flow_dc_to_customer:
    print(f"Flow from {d} to {c}: {flow_dc_to_customer[(d, c)].value()} units")
