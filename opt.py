import pyOpt
import numpy as np
def objfunc(x):
    f = -x[0]*x[1]*x[2]
    g = [0.0]*2
    g[0] = x[0] + 2.*x[1] + 2.*x[2] - 72.0
    g[1] = -x[1] - 2.*x[1] - 2.*x[2]

    fail = 0
    return f,g,fail

opt_prob = pyOpt.Optimization('TP37 Constrained problem',objfunc)
opt_prob.addObj('f')
opt_prob.addVar('x1','c',lower=0.0,upper=42.0,value=10.0)
opt_prob.addVar('x2','c',lower=0.0,upper=42.0,value=10.0)
opt_prob.addVar('x3','c',lower=0.0,upper=42.0,value=10.0)
opt_prob.addConGroup('g',2,'i')

print(opt_prob)

slsqp = pyOpt.SLSQP()
slsqp.setOption('IPRINT',-1)

res = slsqp(opt_prob,sens_type='FD')

print(opt_prob.solution(0))
