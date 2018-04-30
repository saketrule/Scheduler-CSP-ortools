from __future__ import print_function
import sys
from ortools.constraint_solver import pywrapcp

solver = pywrapcp.Solver('schedule_shifts')

# Number of classes and slots
n_classes = 200
n_slots = 220

# Assignment of classes to slot indices
assignment = []
for i in range(n_classes):
    assignment.append(solver.IntVar(0,n_slots-1,"Class %i"%i))

# A slot is only occupied once
solver.Add(solver.AllDifferent(assignment))

# Running the Solver
db = solver.Phase(assignment,solver.CHOOSE_FIRST_UNBOUND,solver.ASSIGN_MIN_VALUE)
solution = solver.Assignment()
solution.Add(assignment)
#collector = solver.AllSolutionCollector(solution)

solver.Solve(db)
#print("Solutions found: ", collector.SolutionCount())
print("Time taken: ", solver.WallTime(), "ms")


#solver.NextSolution()
myvar = 0
while solver.NextSolution():
    print(myvar)
    myvar += 1
    if myvar>100:
        break
'''
for sol in range(collector.SolutionCount()):
    print("\n------------\n")
    print("Solution %i : "%sol)
    asg = []
    for i in range(3):
        asg.append(collector.Value(sol,assignment[i]))
    print(asg)
'''
