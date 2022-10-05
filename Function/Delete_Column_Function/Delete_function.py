import pandas as pd
from datetime import datetime
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from turtle import textinput


class DeleteFunction:
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

        # drop function which is used in removing or deleting rows or columns from the CSV files
        print('Start Deleting Column . . .\n'
              '||')

        # Column name to Delete
        col_File_A = textinput("File A: Input Column To Delete",
                               "Which column do you want to delete?")
        file_A.pop(col_File_A)

        time.sleep(0.5)

        col_File_B = textinput("File B: Input Column To Delete",
                               "Which column do you want to delete?")
        file_B.pop(col_File_B)

        print('Finished Deleting Column\n'
              '||')
        print('Start Exporting Files . . .\n'
              '||')

        file_A.to_csv('Imported Resources/Delete list/Delete Result/' +
                      'Result_file_A.csv', index=False)
        file_B.to_csv('Imported Resources/Delete list/Delete Result/' +
                      'Result_file_B.csv', index=False)

        print('Finished Exporting Files\n'
              '||')

        end_Time = datetime.now()
        print('=================================================\n'
              '||                                             ||\n'
              '||The Program Has Been Successfully Completed  ||\n'
              '||                                             ||\n'
              '=================================================\n'
              "Duration: {}".format(end_Time - start_Time))
