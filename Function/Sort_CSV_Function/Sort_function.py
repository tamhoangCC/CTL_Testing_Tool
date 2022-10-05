import pandas as pd
from datetime import datetime
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename


class SortFunction:
    def Run(self):
      
        start_time = datetime.now()
        print('Start The Program . . .\n'
              '||')

        # Select Files
        Tk().withdraw()

        print('Please Select File A \n'
              '||')
        ask_file_A = askopenfilename()

        time.sleep(0.5)

        print('Please Select File B \n'
              '||')
        ask_file_B = askopenfilename()

        # Read csv files
        print('Reading Files . . .\n'
              '||')

        file_A = pd.read_csv(ask_file_A,
                             dtype=str, low_memory=False, delimiter=',', keep_default_na=False, na_filter=False)
        file_B = pd.read_csv(ask_file_B,
                             dtype=str, low_memory=False, delimiter=',', keep_default_na=False, na_filter=False)

        print('Finished Reading Files\n'
              '||')

        # Check header
        print('Preparing . . .')
        check_Header_file_A = list(file_A.columns)
        check_Header_file_B = list(file_B.columns)

        print(check_Header_file_A)
        print(check_Header_file_B)

        # Get header
        get_Header_file_A = check_Header_file_A
        get_Header_file_B = check_Header_file_B

        # Sort
        print('Start Sorting . . .\n'
              '||')

        sort_file_1 = file_A.sort_values(
            get_Header_file_A, axis=0, ascending=True)
        sort_file_2 = file_B.sort_values(
            get_Header_file_B, axis=0, ascending=True)

        print('Finished Sorting\n'
              '||')

        # Export sort result
        print('Start Exporting Files . . .\n'
              '||')

        sort_file_1.to_csv('Imported Resources/Sort list/Sort Result/' +
                           'Sort_Result_File_Daily.csv', index=False)
        sort_file_2.to_csv('Imported Resources/Sort list/Sort Result/' +
                           'Sort_Result_File_Backup.csv', index=False)

        print('Finished Exporting Files\n'
              '||')

        #
        end_Time = datetime.now()
        print('=================================================\n'
              '||                                             ||\n'
              '||The Program Has Been Successfully Completed  ||\n'
              '||                                             ||\n'
              '=================================================\n'
              "Duration: {}".format(end_Time - start_time))
