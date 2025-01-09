from MILP import *

def check_free(x1,y2,expression):
    t3=[]
    for i in range(64):
        if i not in x1:
            t3.append(i)

    t1 = expression.split("+")

    t2 = []
    for i in t1:
        for j in range(64):
            if "[" + str(j) + "][0]" in i:
                if j not in t2:
                    t2.append(j)

    x_in_y=[]
    for i in y2:
        for j in t2:
            if (i+j)%64 not in x_in_y:
                x_in_y.append((i+j)%64)

    for i in t3:
        if i in x_in_y:
            continue
        else:
            print(i,"不在线性方程中")
    print(len(x_in_y))

def get_x_time(expression):

    t1 = expression.split("+")
    t2 = []
    for i in t1:
        if "*" in i:
            if count_char(i, "x") >= 1:
                t2.append(i)

    x_time = []
    for i in t2:
        t = []
        for x in range(64):
            if "[" + str(x) + "][0]" in i:
                t.append([x, 1])
        x_time.append(t)
    return x_time

def count_char(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

with open('output.txt', 'r', encoding='utf-8') as file:
    expression1=file.read()

x_time=get_x_time(expression1)
result=[]
count_n2=34

m=gp.Model("mip1")
X=variable_1(m,64)
Y=variable_1(m,64)
for x in range(64):
    for i in x_time:
        t=[]
        for j in i:
            if j[1]>=2:
                eq = [[1, -1, 0]]
                constr(m,[X[(j[0]+x)%64],Y[x]],eq)
            else:
                t.append(j[0])
        if len(t)>=2:
            m.addConstr(gp.quicksum([X[(k+x)%64] for k in t])>=(len(t)-1)*Y[x])

m.addConstr(gp.quicksum(Y)==count_n2)
m.addConstr(X[0]==1)
m.addConstr(X[63]==0)
m.setObjective(gp.quicksum(X), GRB.MINIMIZE)

m.optimize()

result.append([sum([X[i].X for i in range(64)]),count_n2])
print("the number of gussed variables：",sum([X[i].X for i in range(64)]))
print("the number of linarized ouput bits：",count_n2)
print(result)

t=[]
t2=[]
for x in range(64):
    if X[x].X==1:
        t.append(x)
    if Y[x].X==1:
        t2.append(x)

print("gussed_var：",t)
print("linearized_output：",t2)

check_free(t,t2,expression1)