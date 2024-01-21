# Statistics calculator
import numpy as np
import pandas as pd

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]


#Convert list into matrix
array = np.array(x)
matrix = np.array(x).reshape(3,3)

#Flattened results
"""sum = np.sum(matrix)  
max = np.max(matrix)
min = np.min(matrix)
sigma = np.std(matrix)
mean = np.mean(matrix)
var = np.var(matrix)"""

stats = ["mean", "variance", "standard deviation", "max", "min", "sum"]
print(matrix)

#Columns
sum_axis0 = []
#sum_axis1 = []

for k in range(3):
    sum_axis0.append(np.sum(matrix[:,k]))
    #sum_axis1.append(np.sum(matrix[k,:]))
sum = pd.Series()
print(sum_axis0)


#print(col)



""" for i in range(0,2):
    mean[i]
for k, v in zip(stats, matrix[0:]):
    print(k,v) """


#Convert results into dictionary

