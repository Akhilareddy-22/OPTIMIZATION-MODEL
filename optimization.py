import pandas as pd
from pulp import *

# Load data
data = pd.read_csv("data/input_data.csv")

# Extract values
profit_A = data.loc[0, "Profit"]
profit_B = data.loc[1, "Profit"]

labor_A = data.loc[0, "Labor"]
labor_B = data.loc[1, "Labor"]

machine_A = data.loc[0, "Machine"]
machine_B = data.loc[1, "Machine"]

labor_limit = data.loc[2, "Labor"]
machine_limit = data.loc[2, "Machine"]

# Create model
model = LpProblem("Optimization_Model", LpMaximize)

# Decision variables
A = LpVariable("Product_A", lowBound=0, cat="Integer")
B = LpVariable("Product_B", lowBound=0, cat="Integer")

# Objective function
model += profit_A * A + profit_B * B, "Total_Profit"

# Constraints
model += labor_A * A + labor_B * B <= labor_limit, "Labor_Constraint"
model += machine_A * A + machine_B * B <= machine_limit, "Machine_Constraint"

# Solve
model.solve()

# Print results
print("Status:", LpStatus[model.status])
print("Product A Units:", A.varValue)
print("Product B Units:", B.varValue)
print("Maximum Profit: ₹", value(model.objective))

# Save results
with open("results/output_results.txt", "w") as f:
    f.write(f"Status: {LpStatus[model.status]}\n")
    f.write(f"Product A Units: {A.varValue}\n")
    f.write(f"Product B Units: {B.varValue}\n")
    f.write(f"Maximum Profit: Rs {value(model.objective)}\n")

print("Results saved in results/output_results.txt")