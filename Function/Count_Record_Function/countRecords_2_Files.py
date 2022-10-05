import pandas as pd
from datetime import datetime


start_Time = datetime.now()
#File 1:
# Read csv
results1 = pd.read_csv('../../', low_memory=False)
results2 = pd.read_csv('../../', low_memory=False)


# Get row in csv file (Not include Header)
# File 1
r1 = len(results1)
r2 = len(results2)


SumDataFile1 = r1 + r2
# Get Header in csv
# File 1
data_top1 = list(results1.columns)
data_top2 = list(results2.columns)



print('Result Of File 1')
print('Header File1',data_top1
      ,'Header File2',data_top2
      , sep='\n')
print('________')

print('Number of records file 1: ',SumDataFile1)

end_Time = datetime.now()

print('Duration: {}'.format(end_Time - start_Time))

