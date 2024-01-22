# Statistics calculator
import numpy as np
import pandas as pd

x = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#Convert list into data frame
matrix = np.array(x).reshape(3,3)
d = pd.DataFrame(data=matrix)

#Operating with the data frame
stats = ["mean", "var", "std", "max", "min", "sum"]
flatData = pd.Series(data=x)
flat = flatData.agg(stats)
col = d.agg(stats,axis=0)
row = d.agg(stats,axis=1)

columns = col.to_numpy()
rows = row.to_numpy()
flat = flat.to_numpy()

c = [c.tolist() for c in columns]
rows = np.transpose(rows)
r = [r.tolist() for r in rows]
f = [f.tolist() for f in flat]

calculations = {}
stat = []
for i in range(6):
    stat.append(c[i])
    stat.append(r[i])
    stat.append(f[i])
    new_data = [(stats[i], stat)]
    calculations.update(new_data)
    stat = []

for k,v in calculations.items():
    print(k, ':' ,v)