from sympy import symbols, simplify,expand

def deal_expression(expression, str1):

    expression = expression.replace(" ", "")
    t1 = expression.split("+")


    t3 = []
    for i in t1:
        if i[0] != "x":
            t = i[0:4].split("*")
            if int(t[0]) % 2 != 0:
                if "x" not in i:
                    t = i.replace(t[0], "1")
                else:
                    t = i.replace(t[0] + "*", "")
                t3.append(t)
        else:
            t3.append(i)

    t4 = []
    for i in t3:
        if "**" in i:
            t = i
            for j in range(2, 10):
                t = t.replace("**" + str(j), "")
            t4.append(t)
        else:
            t4.append(i)

    t = ""
    for i in range(len(t4)):
        if i == 0:
            t = t4[i]
        else:
            t = t + "+" + t4[i]

    with open(str1 + '.txt', 'w') as file:
        file.write(t)


rounds=3

X=[]
for x in range(64):
    t2=[]
    for y in range(5):
        t2.append(symbols('x'+"["+str(x)+"]"+"["+str(y)+"]"))
    X.append(t2)

temp_X=[]
temp_Y=[]

for r in range(rounds):
    if r==0:
        t1 = []
        for x in range(64):
            t2=[]
            for y in range(5):
                t2.append(X[x][y])
            t1.append(t2)
        temp_X .append(t1)

        t1 = []
        for x in range(64):
            t2=[]
            for y in range(5):
                if y==0:
                    t2.append(temp_X[r][x][0])
                if y==1:
                    t2.append(temp_X[r][x][0])
                if y==2:
                    t2.append(1)
                if y==3:
                    t2.append(temp_X[r][x][0])
                if y==4:
                    t2.append(0)
            t1.append(t2)
        temp_Y .append(t1)

    else:
        t1 = []
        for x in range(64):
            t2 = []
            for y in range(5):
                if y == 0:
                    t2.append(temp_Y[r - 1][x][y] + temp_Y[r - 1][(64 + x - 19) % 64][y] + temp_Y[r - 1][(64 + x - 28) % 64][y])
                if y == 1:
                    t2.append(temp_Y[r - 1][x][y] + temp_Y[r - 1][(64 + x - 61) % 64][y] + temp_Y[r - 1][(64 + x - 39) % 64][y])
                if y==2:
                    t2.append(temp_Y[r - 1][x][y] + temp_Y[r - 1][(64 + x - 1)  % 64][y] + temp_Y[r - 1][(64 + x - 6)  % 64][y])
                if y == 3:
                    t2.append(temp_Y[r - 1][x][y] + temp_Y[r - 1][(64 + x - 10) % 64][y] + temp_Y[r - 1][(64 + x - 17) % 64][y])
                if y==4:
                    t2.append(temp_Y[r - 1][x][y] + temp_Y[r - 1][(64 + x - 7)  % 64][y] + temp_Y[r - 1][(64 + x - 41) % 64][y])
            t1.append(t2)
        temp_X.append(t1)

        t1 = []
        for x in range(64):
            t2=[]
            for y in range(5):
                if y==0:
                    t2.append(temp_X[r][x][4]*temp_X[r][x][1] + temp_X[r][x][3] + temp_X[r][x][2]*temp_X[r][x][1] + temp_X[r][x][2] + temp_X[r][x][1]*temp_X[r][x][0] + temp_X[r][x][1] + temp_X[r][x][0])
                if y==1:
                    t2.append(temp_X[r][x][4] + temp_X[r][x][3]*temp_X[r][x][2] + temp_X[r][x][3]*temp_X[r][x][1] + temp_X[r][x][3] + temp_X[r][x][2]*temp_X[r][x][1] + temp_X[r][x][2] + temp_X[r][x][1] + temp_X[r][x][0])
                if y==2:
                    t2.append(temp_X[r][x][4]*temp_X[r][x][3] + temp_X[r][x][4] + temp_X[r][x][2] + temp_X[r][x][1] + 1)
                if y==3:
                    t2.append(temp_X[r][x][4]*temp_X[r][x][0] + temp_X[r][x][4] + temp_X[r][x][3]*temp_X[r][x][0] + temp_X[r][x][3] + temp_X[r][x][2] + temp_X[r][x][1] + temp_X[r][x][0])
                if y==4:
                    t2.append(temp_X[r][x][4]*temp_X[r][x][1] + temp_X[r][x][4] + temp_X[r][x][3] + temp_X[r][x][1]*temp_X[r][x][0] + temp_X[r][x][1])
            t1.append(t2)
        temp_Y .append(t1)


expand_expr_1=expand(temp_Y[rounds-1][0][0])

deal_expression(str(expand_expr_1),"output")


