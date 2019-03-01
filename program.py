##continued fraction
cf =  [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
cf2 = [1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]

##initialisation matrix
im = [0, 0, 0, 1, 1, 0, 0, 0]

##current matrix
cm = []

##output
op = []

def initialise_matrix():
    temp_arr = []

    for x in reversed(cf):
        temp_arr.append(x)

    temp_arr += " "
    temp_arr += " "

    cm.append(temp_arr)

    for a in range(int(len(im)/2)):
        temp_arr = []
        for y in range(len(cf)-1):
            temp_arr += " "

        for z in im[2*a:2*(a+1)]:
            temp_arr.append(z)
        temp_arr += " "

        cm.append(temp_arr)

    print_table()

def initialise_matrix_2():
    temp_arr = []

    for x in reversed(cf):
        temp_arr.append(x)

    cm.append(temp_arr)

    for a in range(int(len(im)/2)):
        temp_arr = []
        for y in range(len(cf)-1):
            temp_arr += " "

        for z in im[2*a:2*(a+1)]:
            temp_arr.append(z)

        if a == 2:
            temp_arr.append(cf2[0])
        else:
            temp_arr.append(" ")

        cm.append(temp_arr)

    for a in range(len(cf2)-1):
        temp_arr = []
        for y in range(len(cf)+1):
            temp_arr += " "

        temp_arr.append(cf2[a+1])
        cm.append(temp_arr)

        temp_arr = []
        for y in range(len(cf)+2):
            temp_arr += " "
            
        cm.append(temp_arr)

    print_table()

def cal_test_2():
    ## current column
    cc = 1
    ## current row
    cr = 1
    ## row spacer
    rs = 0

    ## lazy
    last_shift = False

    #min(len(cf), len(cf2))
    for x in range(1,35):
        #if denominator is 0 left shift
        toprow = (cr//2 + 1)*rs +cr
        if (cm[toprow+1][-(cc+1)] == 0 or cm[toprow+3+rs][-(cc+1)] == 0 or
            cm[toprow+1][-(cc+2)] == 0 or cm[toprow+3+rs][-(cc+2)] == 0):
            if not last_shift:
                y_shift(cc, toprow, cr, rs)

                cr += 2
                last_shift = True
                
            else:
                x_shift(toprow,cc,rs)
            
                cc += 1
                last_shift = False
        
        elif(cm[toprow][-(cc+2)]//cm[toprow+1][-(cc+2)]!= cm[toprow+2+rs][-(cc+2)]//cm[toprow+3+rs][-(cc+2)]):
           
            y_shift(cc, toprow,cr, rs)
            
            cr += 2
        ## if need a x shift 
        elif(cm[toprow+rs+2][-(cc+1)]//cm[toprow+rs+3][-(cc+1)] != cm[toprow+rs+2][-(cc+2)]//cm[toprow+rs+3][-(cc+2)]):
            x_shift(toprow,cc,rs)
            
            cc += 1
        
        else:
            #Have a euclidean step
            output = cm[toprow][-(cc+2)]//cm[toprow+1][-(cc+2)]
            op.append(output)
            ## Calculate the next values
            x1 = cm[toprow][-(cc+2)] - output*cm[toprow+1][-(cc+2)]
            x2 = cm[toprow][-(cc+1)] - output*cm[toprow+1][-(cc+1)]
            x3 = cm[toprow+rs+2][-(cc+2)] - output*cm[toprow+rs+3][-(cc+2)]
            x4 = cm[toprow+rs+2][-(cc+1)] - output*cm[toprow+rs+3][-(cc+1)]

            
            for x in range(len(cf2)):
                ## Empty row
                temp_arr = []
                for space in range(len(cf)+2):
                    temp_arr += " "
                if(x == (cr//2)):
                    temp_arr[-(cc+1)] = x2
                    temp_arr[-(cc+2)] = x1
                elif(x == ((cr//2)+1)):
                    temp_arr[-(cc+1)] = x4
                    temp_arr[-(cc+2)] = x3

                cm.insert((x+1)*(3+rs), temp_arr)
                

            rs += 1
            
            print("output = " + str(op))
        

        
        #print_table()

    ## New output if (ab)(cd)(ef)(gh) a/c == e/g and e/g == f/h
   
    ## If left integer parts are equivalent
    #if cm[][] // cm[][] == cm[][] // cm[][] && cm[][] // cm[][] == cm[][] // cm[][]


    pass;


def y_shift(cc, toprow, cr, rs):
    
    cm[toprow+4+2*rs][-(cc+1)] = cm[toprow+2+rs][-(cc+1)]*cf2[cr//2] + cm[toprow][-(cc+1)]
    cm[toprow+4+2*rs][-(cc+2)] = cm[toprow+2+rs][-(cc+2)]*cf2[cr//2] + cm[toprow][-(cc+2)]
    cm[toprow+5+2*rs][-(cc+2)] = cm[toprow+3+rs][-(cc+2)]*cf2[cr//2] + cm[toprow+1][-(cc+2)]
    cm[toprow+5+2*rs][-(cc+1)] = cm[toprow+3+rs][-(cc+1)]*cf2[cr//2] + cm[toprow+1][-(cc+1)]
    
def x_shift(toprow,cc,rs):
    
    cm[toprow][-(cc+3)] = cm[toprow][-(cc+2)]*cm[0][-(cc)]+cm[toprow][-(cc+1)]
    cm[toprow+1][-(cc+3)] = cm[toprow+1][-(cc+2)]*cm[0][-(cc)]+cm[toprow+1][-(cc+1)]
    cm[toprow+2+rs][-(cc+3)] = cm[toprow+2+rs][-(cc+2)]*cm[0][-(cc)]+cm[toprow+2+rs][-(cc+1)]
    cm[toprow+3+rs][-(cc+3)] = cm[toprow+3+rs][-(cc+2)]*cm[0][-(cc)]+cm[toprow+3+rs][-(cc+1)]
    
def cal_test():
    cr = 2
    cc = 0
    for x in range(1,len(cf)):
        
        cm[cr-1][-(x+2)] = cm[cr-1][-(x+1)]*cm[0][-(x)]+cm[cr-1][-x]
        cm[cr][-(x+2)] = cm[cr][-(x+1)]*cm[0][-(x)]+cm[cr][-x]

        if (cm[cr][-(x+2)] != 0) & (cm[cr][-(x+1)] != 0):
            if cm[cr-1][-(x+2)]/cm[cr][-(x+2)] > cm[cr-1][-(x+1)]/cm[cr][-(x+2)]:
                nextint = int((cm[cr-1][-(x+1)]/cm[cr][-(x+1)])//1)

                temp_arr = []
                for y in range(len(cf)-(x+1)):
                    temp_arr += " "
                temp_arr.append(int(cm[cr-1][-(x+2)] - cm[cr][-(x+2)]*nextint))
                temp_arr.append(int(cm[cr-1][-(x+1)] - cm[cr][-(x+1)]*nextint))
                for y in range(cr-1):
                    temp_arr += " "
                temp_arr.append(nextint)
                cm.append(temp_arr)
  
                cr += 1
                cc += 1

    print_table()
    print_latex()
    
def print_table():
    temp = ""
    for x in cm:
        if not checkEqual2(x):
            for y in x:
                temp += '{:6s}'.format(str(y))
            temp += "\n"

    print(temp)

def checkEqual2(iterator):
   return len(set(iterator)) <= 1

def print_latex():

    temp = "\\begin{center}\n\\begin{tabular}{||c c"
    for z in cm[0]:
        temp+= "c "
    temp += "||}\\hline \n"
    for x in cm:
        if not checkEqual2(x):
            for y in range(len(x)):
                if x[y] == len(x):
                    temp += str(x[y])
                else:
                    temp += str(x[y]) + "&"
            
            temp += "\\\\ \n"

    temp+="\\hline \n\\end{tabular} \n\\end{center}"

    print(temp)
    

initialise_matrix_2()
cal_test_2()
print_table()
print_latex()
