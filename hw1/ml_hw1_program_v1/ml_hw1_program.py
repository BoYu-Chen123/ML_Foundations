import pandas as pd
import numpy as np
import sys

############read data
def read_data(X0, scale):
    Data = []
    Y = []
    filename = sys.argv[1]
    for lines in open(filename).readlines():
        temp = lines.strip().split()
        X = [X0 / scale]
        for i in range(len(temp)-1):
            X.append((float(temp[i])) / scale)
        Y.append(float(temp[-1]))
        Data.append(X)
    return Data, Y

############PLA
def PLA(problem, Data, Y):
    Stop_thresh = 500
    num_Data = len(Data)
    iteration_list = []
    w0_list = []
    for k in range(1000):
        print(k, end='\r')
        w = np.zeros([11], dtype=float)
        stop = 0
        iteration = 0
        while stop != Stop_thresh:
            pick = np.random.randint(num_Data)
            inner = np.dot(w, Data[pick])
            if (Y[pick]*np.sign(inner)<0 ) | ((Y[pick]==1) & (np.sign(inner)==0)):
                stop = 0
                iteration += 1
                if Y[pick] == 1:
                    w += Data[pick]
                elif Y[pick] == -1:
                    w -= Data[pick]
            else:
                stop += 1
        iteration_list.append(iteration)
        w0_list.append(w[0])
    print("problem " + str(problem) + " : iteration_median " + str(np.median(iteration_list)))
    if problem==16:
        print("problem " + str(problem+1) + " : w0_median " + str(np.median(w0_list)))

Data16, Y16 = read_data(1, 1)
PLA(16, Data16, Y16)
Data18, Y18 = read_data(10, 1)
PLA(18, Data18, Y18)
Data19, Y19 = read_data(0, 1)
PLA(19, Data19, Y19)
Data20, Y20 = read_data(0, 4)
PLA(20, Data20, Y20)