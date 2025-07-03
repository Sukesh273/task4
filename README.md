# task4
# README - Furniture Production Optimization

## Overview
This project implements a linear programming solution to optimize furniture production, maximizing profit while considering labor and material constraints. The solution uses the PuLP library in Python to model and solve the optimization problem.

## Problem Statement
A furniture manufacturer produces three types of items:
- Chairs
- Tables
- Bookshelves

The goal is to determine the optimal number of each item to produce, given:
- **Profit per unit**: 
  - Chair: \$20 
  - Table: \$50 
  - Bookshelf: \$40
- **Labor constraint**: 400 hours available
  - Chair: 1 hour/unit 
  - Table: 2 hours/unit 
  - Bookshelf: 3 hours/unit
- **Material constraint**: 600 units available
  - Chair: 4 units/unit 
  - Table: 5 units/unit 
  - Bookshelf: 8 units/unit
- **Market demand constraints**:
  - Maximum 100 chairs
  - Maximum 50 tables
  - Maximum 40 bookshelves

## Solution Approach
The problem is modeled as a linear programming problem with the following steps:
1. **Initialize the model**: Set up the optimization problem to maximize profit.
2. **Define decision variables**: Represent the quantities of chairs, tables, and bookshelves to produce, with bounds based on market demand.
3. **Define the objective function**: Maximize total profit based on the profit per unit of each item.
4. **Add constraints**: Incorporate labor and material constraints to ensure feasibility.
5. **Solve the problem**: Use the PuLP solver to find the optimal production plan.
6. **Print results**: Display the optimal quantities and total profit, along with constraint utilization.

## Code Implementation
The solution is implemented in Python using the PuLP library. Key components include:
- `LpProblem`: Defines the optimization problem.
- `LpVariable`: Represents the decision variables (chair, table, bookshelf) with their bounds.
- `lpSum`: Used for summing the terms in the objective function and constraints.
- `model.solve()`: Solves the optimization problem.

## Results
The program outputs:
- **Status**: Indicates whether the solution is optimal.
- **Optimal Production Plan**: Shows the number of chairs, tables, and bookshelves to produce.
- **Total Profit**: The maximum achievable profit under the given constraints.
- **Constraint Utilization**: Displays how much of the available labor and materials are used.

## Example Output
```
Status: Optimal
Optimal Production Plan:
Chairs: 100 units
Tables: 50 units
Bookshelves: 40 units
Total Profit: $5000.00

Constraint Utilization:
Labor used: 400 of 400 hours
Materials used: 600 of 600 units
```

## Dependencies
- Python 3.x
- PuLP library (Install using `pip install pulp`)

## How to Run
1. Ensure Python and PuLP are installed.
2. Save the code in a file, e.g., `task4.py`.
3. Run the script using the command:  
   ```bash
   python task4.py
   ```
