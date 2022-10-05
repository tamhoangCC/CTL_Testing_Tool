import pandas as pd
from datetime import datetime
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename


class CountColumnFunction:
    def Run(self):
        start_time = datetime.now()
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

        print('Start Counting Column . . .\n'
              '||')
        count_col_fileA = len(file_A.columns)
        count_col_fileB = len(file_B.columns)

        print('Finished Counting Column\n'
              '||')

        print('Total Number Of Columns Of File A: ', count_col_fileA)
        print('Total Number Of Columns Of File B: ', count_col_fileB)

        print('||')

        end_Time = datetime.now()
        print('=================================================\n'
              '||                                             ||\n'
              '||The Program Has Been Successfully Completed  ||\n'
              '||                                             ||\n'
              '=================================================\n'
              "Duration: {}".format(end_Time - start_time))
