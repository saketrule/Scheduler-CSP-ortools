from __future__ import print_function
import sys
from ortools.constraint_solver import pywrapcp

solver = pywrapcp.Solver('schedule_shifts')

fri = [True,False,False,False]


ri = solver.IntVar(0,1,"r")
ti = solver.IntVar(0,1,"t")

solver.Add((ri+ti).IndexOf(fri)==True)
solver.Add(solver.AllDifferent([ri,ti]))


db = solver.Phase([ri,ti],solver.CHOOSE_FIRST_UNBOUND,solver.ASSIGN_MIN_VALUE)
solution = solver.Assignment()
#solution.Add(assignment)
solver.Solve(db)
print("Time taken: ", solver.WallTime(), "ms")

while solver.NextSolution():
    print(ri,ti)
