import pandas as pd
import glob
import os


class MergeFunction:
    def Run(self):

        # merge two file
        df = pd.concat(
            map(pd.read_csv, ['../../',
                              '../../']

                ), ignore_index=True)

        print(df)
