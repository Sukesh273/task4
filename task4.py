# from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus

# # 1. Initialize the model
# model = LpProblem("Furniture_Production_Optimization", LpMaximize)

# # 2. Define decision variables
# chair = LpVariable('Chair', lowBound=0, upBound=100, cat='Integer')  # upBound from market demand
# table = LpVariable('Table', lowBound=0, upBound=50, cat='Integer')
# bookshelf = LpVariable('Bookshelf', lowBound=0, upBound=40, cat='Integer')

# # 3. Define objective function (maximize profit)
# model += 20 * chair + 50 * table + 40 * bookshelf, "Total Profit"

# # 4. Add constraints
# # Labor constraint: 1*chair + 2*table + 3*bookshelf <= 400
# model += 1 * chair + 2 * table + 3 * bookshelf <= 400, "Labor_Constraint"

# # Materials constraint: 4*chair + 5*table + 8*bookshelf <= 600
# model += 4 * chair + 5 * table + 8 * bookshelf <= 600, "Materials_Constraint"

# # 5. Solve the problem
# model.solve()

# # 6. Print results
# print(f"Status: {LpStatus[model.status]}")
# print(f"Optimal Production Plan:")
# print(f"Chairs: {chair.value()} units")
# print(f"Tables: {table.value()} units")
# print(f"Bookshelves: {bookshelf.value()} units")
# print(f"Total Profit: ${model.objective.value():.2f}")

# # 7. Print constraint utilization
# print("\nConstraint Utilization:")
# print(f"Labor used: {1*chair.value() + 2*table.value() + 3*bookshelf.value()} of 400 hours")
# print(f"Materials used: {4*chair.value() + 5*table.value() + 8*bookshelf.value()} of 600 units")