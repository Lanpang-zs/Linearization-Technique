
import gurobipy as gp
from gurobipy import GRB

def variable_1(m,R):
    X = []
    for r in range(R):
        X.append(m.addVar(vtype=GRB.BINARY))
    return X
def variable_2(m,R,x):
    X = []
    for r in range(R):
        t=[]
        for i in range(x):
            t.append(m.addVar(vtype=GRB.BINARY))
        X.append(t)
    return X
def variable_3(m,R,x,y):
    X = []
    for r in range(R):
        t=[]
        for i in range(x):
            t1 = []
            for j in range(y):
                t1.append(m.addVar(vtype=GRB.BINARY))
            t.append(t1)
        X.append(t)
    return X
def variable_4(m,R,x,y,z):
    X = []
    for r in range(R):
        t=[]
        for i in range(x):
            t1 = []
            for j in range(y):
                t2 = []
                for k in range(z):
                    t2.append(m.addVar(vtype=GRB.BINARY))
                t1.append(t2)
            t.append(t1)
        X.append(t)
    return X
def variable_5(m,R,x,y,z,d):
    X = []
    for r in range(R):
        t=[]
        for i in range(x):
            t1 = []
            for j in range(y):
                t2 = []
                for k in range(z):
                    t3 = []
                    for l in range(d):
                        t3.append(m.addVar(vtype=GRB.BINARY))
                    t2.append(t3)
                t1.append(t2)
            t.append(t1)
        X.append(t)
    return X

def constr(m,x,eq):
    for i in range(len(eq)):
        t = gp.LinExpr()
        for j in range(len(x)):
            t+=x[j]*eq[i][j]
        t+=eq[i][len(x)]
        m.addConstr(t>=0)
    return m


