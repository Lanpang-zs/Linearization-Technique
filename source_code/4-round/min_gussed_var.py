from MILP import *

def count_char(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

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



with open('T0.txt', 'r', encoding='utf-8') as file:

    expression1=file.read()

with open('X_1^4.txt', 'r', encoding='utf-8') as file:

    expression2=file.read()

with open('T1.txt', 'r', encoding='utf-8') as file:

    expression3=file.read()

x_time1=get_x_time(expression1)
x_time2=get_x_time(expression2)
x_time3=get_x_time(expression3)


start_X=[]
start_Y=[]

result=[]
for count_n2 in range(1,65):
    m=gp.Model("mip1")
    X=variable_1(m,64)
    Y=variable_1(m,64)

    for x in range(64):
        for i in x_time1:
            t=[]
            for j in i:
                t.append(j[0])
            if len(t)>=2:
                m.addConstr(gp.quicksum([X[(k+x)%64] for k in t])>=(len(t)-1)*Y[x])

        for i in x_time2:
            t=[]
            for j in i:
                t.append(j[0])
            if len(t)>=1:
                m.addConstr(gp.quicksum([X[(k+x)%64] for k in t])>=(len(t))*Y[x])

        for i in x_time3:
            t=[]
            for j in i:
                t.append(j[0])
            if len(t)>=1:
                m.addConstr(gp.quicksum([X[(k+x)%64] for k in t])>=(len(t)-1)*Y[x])

    m.addConstr(gp.quicksum(Y)==count_n2)
    m.addConstr(X[0]==1)
    m.addConstr(X[63]==0)



    m.setObjective(gp.quicksum(X), GRB.MINIMIZE)
    m.Params.timeLimit = 60
    m.optimize()

    result.append([count_n2, sum([X[i].X for i in range(64)])])
    print("the number of gussed variables：", sum([X[i].X for i in range(64)]))
    print("the number of linarized ouput bits：", count_n2)

    t1=[];t2=[]
    for i in range(64):
        t1.append(X[i].X)
        t2.append(Y[i].X)
    start_X.append(t1)
    start_Y.append(t2)

    with open("start_X.txt", 'w') as file:
        file.write(str(start_X))
    with open("start_Y.txt", 'w') as file:
        file.write(str(start_Y))

t=[];t2=[]
for x in range(64):
    if X[x].X==1:
        t.append(x)
    if Y[x].X==1:
        t2.append(x)

print("gussed_var：",t)
print("linearized_output：",t2)