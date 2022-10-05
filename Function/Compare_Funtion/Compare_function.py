import pandas as pd
import time
from datetime import datetime
from tkinter import Tk
from tkinter.filedialog import askopenfilename


class CompareFunction:
    def Run(self):
        start_Time = datetime.now()

        print('Start The Program . . .\n'
              '||')

        # Select Files
        Tk().withdraw()

        print('Please Select File A \n'
              '||')

        ask_file_A = askopenfilename()

        time.sleep(1)

        print('Please Select File B \n'
              '||')

        ask_file_B = askopenfilename()

        file_A = pd.DataFrame([])
        file_B = pd.DataFrame([])

        # read_csv
        print('Reading Files . . .\n'
              '||')
        file_A = pd.read_csv(ask_file_A,
                             dtype=str, low_memory=False, delimiter=',', keep_default_na=False, na_filter=False)

        file_B = pd.read_csv(ask_file_B,
                             dtype=str, low_memory=False, delimiter=',', keep_default_na=False, na_filter=False)

        print('Finished Reading Files\n'
              '||')

        # Handle value 'nan'
    #   for row in file_A.itertuples(index=False):
    #       if (row[1] == 'nan'):
    #           print("NULL VALUE")

        # Compare
        print('Start Comparing Files . . .\n'
              '||')
        result1 = file_A[~file_A.apply(
            tuple, 1).isin(file_B.apply(tuple, 1))]
        print('result1: ', )
        result2 = file_B[~file_B.apply(
            tuple, 1).isin(file_A.apply(tuple, 1))]

        print('Finished Comparing Files\n'
              '||')
        # print("File A original",file_A, '\n\n')
        # print("File B original",file_B, '\n\n')
        #
        # print("File A vs B: ",result1, '\n\n')
        # print("File B vs A: ",result2, '\n\n')

        # Output
        print('Start Exporting Files . . .\n'
              '||')
        result1.to_csv(
            'Imported Resources/Compare list/Compare Result/' + 'Result_compare_data_in_Daily.csv', index=False)
        result2.to_csv(
            'Imported Resources/Compare list/Compare Result/' + 'Result_compare_data_in_Backup.csv', index=False)

        print('Finished Exporting Files\n'
              '||')

        end_Time = datetime.now()
        print('=================================================\n'
              '||                                             ||\n'
              '||The Program Has Been Successfully Completed  ||\n'
              '||                                             ||\n'
              '=================================================\n'
              "Duration: {}".format(end_Time - start_Time))
