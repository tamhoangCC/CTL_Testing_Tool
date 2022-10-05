import pandas as pd
from datetime import datetime
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename


class SortAndCompareFunction:
    def Run(self):

        start_time = datetime.now()
        print('Start The Program . . .\n'
              '||')

        # STEP 1: SORT FILE
        ######################################################################################################
        print('Start Sorting Files Function . . .\n'
              '||')

        # Select Files
        Tk().withdraw()

        print('Please Select File Daily \n'
              '||')
        ask_file_Daily = askopenfilename()

        time.sleep(0.5)

        print('Please Select File Backup \n'
              '||')
        ask_file_Backup = askopenfilename()

        # Read csv files to sort
        print('Reading Files . . .\n'
              '||')

        file_Daily = pd.DataFrame([])
        file_Backup = pd.DataFrame([])

        file_Daily = pd.read_csv(ask_file_Daily,
                                 dtype=str, low_memory=False, delimiter=',', keep_default_na=False, na_filter=False)
        file_Backup = pd.read_csv(ask_file_Backup,
                                  dtype=str, low_memory=False, delimiter=',', keep_default_na=False, na_filter=False)

        print('Finished Reading Files\n'
              '||')

        # Check header
        print('Preparing . . .\n'
              '||')
        # Note a File must have Header to sort
        check_Header_file_Daily = list(file_Daily.columns)
        check_Header_file_Backup = list(file_Backup.columns)

        print('Header File Daily:\n', check_Header_file_Daily)
        print('Header File Backup:\n', check_Header_file_Backup)

        # Get header
        get_Header_file_Daily = check_Header_file_Daily
        get_Header_file_Backup = check_Header_file_Backup

        # Sort Function
        print('Start Sorting . . .\n'
              '||')

        sort_file_Daily = file_Daily.sort_values(
            get_Header_file_Daily, axis=0, ascending=True)
        sort_file_Backup = file_Backup.sort_values(
            get_Header_file_Backup, axis=0, ascending=True)

        print('Finished Sorting\n'
              '||')

        # Export sort result
        print('Start Exporting Files . . .\n'
              '||')

        sort_file_Daily.to_csv(
            'Imported Resources/Sort and Compare list/Sort Result/' + 'Sort_Result_File_Daily.csv', index=False)
        sort_file_Backup.to_csv(
            'Imported Resources/Sort and Compare list/Sort Result/' + 'Sort_Result_File_Backup.csv', index=False)

        print('Finished Exporting Files\n'
              '||')

        print('Finished Sorting Files Function\n'
              '|| - - - - - - - - - ||\n'
              'MOVING TO NEXT FUNCTION . . .\n'
              '||')

        # STEP 2: COMPARE FILE DAILY AND FILE BACKUP
        ######################################################################################################
        print('Start Comparing Files Function . . .\n'
              '||')

        file_Daily_to_compare = pd.DataFrame([])
        file_Backup_to_compare = pd.DataFrame([])

        # Read file csv to compare
        print('Reading Files . . .\n'
              '||')

        file_Daily_to_compare = pd.read_csv('Imported Resources/Sort and Compare list/Sort Result/Sort_Result_File_Daily.csv',
                                            dtype=str, low_memory=False, delimiter=',', keep_default_na=False, na_filter=False)
        file_Backup_to_compare = pd.read_csv('Imported Resources/Sort and Compare list/Sort Result/Sort_Result_File_Backup.csv',
                                             dtype=str, low_memory=False, delimiter=',', keep_default_na=False, na_filter=False)

        print('Finished Reading Files\n'
              '||')

        # Handle value 'nan'
      #   for row in file_Daily_to_compare.itertuples(index=False):
      #   if (row[1] == 'nan'):
      #       print("NULL VALUE")

        # Compare
        print('Start Comparing Files . . .\n'
              '||')

        result1 = file_Daily_to_compare[~file_Daily_to_compare.apply(
            tuple, 1).isin(file_Backup_to_compare.apply(tuple, 1))]
        result2 = file_Backup_to_compare[~file_Backup_to_compare.apply(
            tuple, 1).isin(file_Daily_to_compare.apply(tuple, 1))]

        # print("File A original",file_A, '\n\n')
        # print("File B original",file_B, '\n\n')
        #
        # print("File A vs B: ",result1, '\n\n')
        # print("File B vs A: ",result2, '\n\n')

        print('Finished Comparing Files\n'
              '||')

        # Output
        print('Start Exporting Files . . .\n'
              '||')

        result1.to_csv('Imported Resources/Sort and Compare list/Compare Result/' +
                       'Result_file_daily.csv', index=False)
        result2.to_csv('Imported Resources/Sort and Compare list/Compare Result/' +
                       'Result_file_backup.csv', index=False)

        print('Finished Exporting Files\n'
              '||')

        print('Finished Comparing Files Function\n'
              '||')

        #
        end_Time = datetime.now()
        print('=================================================\n'
              '||                                             ||\n'
              '||The Program Has Been Successfully Completed  ||\n'
              '||                                             ||\n'
              '=================================================\n'
              "Duration: {}".format(end_Time - start_time))
