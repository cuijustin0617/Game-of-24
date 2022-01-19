def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mult(a, b):
    return a * b
def div(a, b):
    return a / b



def mix(L):
    for i in range(4):
        L1 = L[:]
        a = L1[i]

        for j in range(3):
            L2=L1[:]
            L2.remove(L2[i])
            b = L2[j]

            for k in range(2):
                L3=L2[:]
                L3.remove(L3[j])
                c = L3[k]
                L3.remove(L3[k])
                d = L3[0]
                res = play24([a,b,c,d])
                if res!= None:

                    return play24([a,b,c,d])


def play24(L):
    operations = {'+': add,'-': sub, '*':mult, '/': div}
    op_no_div = {'+': add,'-': sub, '*':mult}
    a=L[0]
    b=L[1]
    c=L[2]
    d=L[3]
    process=[]
    all_solutions = []
    for op1 in operations:
        res1=operations[op1](a,b)
        first_op = op1
        for op2 in operations:
            res2=operations[op2](c,d)
            second_op = op2
            if res2 == 0:
                for op3 in op_no_div:
                    ans=operations[op3](res1,res2)
                    last_op = op3
                    if ans == 24:
                        process = ["1st: "+op1,"2nd: "+op2,op3]
                        #steps = L+process
                        #all_solutions.append(steps)
                        return L+process
            else:
                for op3 in operations:
                    ans=operations[op3](res1,res2)
                    last_op = op3
                    if ans == 24:
                        process = ["first two: "+op1,"last two: "+op2,"final op: "+op3]
                        #steps = L+process
                        #all_solutions.append(steps)
                        return L+process
    for op1 in operations:
        res1=operations[op1](a,b)
        first_op = op1
        for op2 in operations:
            res2=operations[op2](res1,c)
            second_op=op2
            for op3 in operations:
                ans = operations[op3](res2,d)
                last_op = op3
                if ans == 24:
                    process = ["1st:"+op1,"2nd:"+op2,"3rd:"+op3]
                    #steps = L+process
                    #all_solutions.append(steps)
                    return L+process
    for op1 in operations:
        res1=operations[op1](b,c)
        first_op = op1
        for op2 in operations:
            res2=operations[op2](res1,d)
            second_op=op2
            if res2 == 0:
                for op3 in op_no_div:
                    ans=operations[op3](a,res2)
                    last_op = op3
                    if ans == 24:
                        process = ["bet bc:"+op1,"withd:"+op2,"1st with:"+op3]
                        return L+process
            else:

                for op3 in operations:
                    ans = operations[op3](a,res2)
                    last_op = op3
                    if ans == 24:
                        process = ["bet bc:"+op1,"withd:"+op2,"1st with:"+op3]
                        #steps = L+process
                        #all_solutions.append(steps)
                        return L+process
    for op1 in operations:
        res1=operations[op1](c,d)
        first_op = op1
        if res1 == 0:
            for op2 in op_no_div:
                res2=operations[op2](b,res1)
                second_op=op2
                if res2 == 0:
                    for op3 in op_no_div:
                        ans=operations[op3](a,res2)
                        last_op = op3
                        if ans == 24:
                            process = ["bet cd:"+op1,"b with:"+op2,"a with:"+op3]
                            return L+process
                else:

                    for op3 in operations:
                        ans = operations[op3](a,res2)
                        last_op = op3
                        if ans == 24:
                            process = ["bet cd:"+op1,"b with:"+op2,"a with:"+op3]
                            #steps = L+process
                            #all_solutions.append(steps)
                            return L+process
        else:
            for op2 in operations:
                res2=operations[op2](b,res1)
                second_op=op2
                if res2 == 0:
                    for op3 in op_no_div:
                        ans=operations[op3](a,res2)
                        last_op = op3
                        if ans == 24:
                            process = ["bet cd:"+op1,"b with:"+op2,"a with:"+op3]
                            return L+process
                else:

                    for op3 in operations:
                        ans = operations[op3](a,res2)
                        last_op = op3
                        if ans >= 23.9 and ans<=24.1:
                            process = ["bet cd:"+op1,"b with:"+op2,"a with:"+op3]
                            #steps = L+process
                            #all_solutions.append(steps)
                            return L+process



    return None












#print(mix([6,9,8,10]))