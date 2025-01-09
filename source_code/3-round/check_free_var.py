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

with open('output.txt', 'r', encoding='utf-8') as file:

    expression1=file.read()

t1=[0, 1, 3, 4, 6, 7, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25, 26, 27, 28, 29, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 45, 46, 48, 49, 50, 51, 52, 53, 55, 56, 57, 58, 59, 60, 61, 62]
t2=[1, 10, 17, 20, 23, 42, 45, 52, 53, 56, 59, 62]


check_free(t1,t2,expression1)
