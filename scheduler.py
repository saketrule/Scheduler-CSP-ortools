from __future__ import print_function
import sys
from ortools.constraint_solver import pywrapcp

solver = pywrapcp.Solver('schedule_shifts')



db = solver.Phase([ri,ti],solver.CHOOSE_FIRST_UNBOUND,solver.ASSIGN_MIN_VALUE)
solution = solver.Assignment()
#solution.Add(assignment)
solver.Solve(db)
print("Time taken: ", solver.WallTime(), "ms")

while solver.NextSolution():
    print(ri,ti)
