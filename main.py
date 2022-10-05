from tkinter.ttk import Style
from turtle import numinput
import turtle
import Function.Compare_Funtion as compre_file
import Function.Count_Column_Function as count_column
import Function.Count_Record_Function as count_record
import Function.Delete_Column_Function as delete_column
import Function.Merge_CSV_Function as merge_file
import Function.Sort_and_Compare_Function as sort_and_compare
import Function.Sort_CSV_Function as sort_file


class mainprogram:
    def Run():

        ui_style = turtle.title('Instructions For Choosing Function')
        ui_style = turtle.penup()
        ui_style = turtle.goto(250, 100)
        # ui_style = turtle.pendown()
        # ui_style = turtle.color('black')
        style = ('Courier', 20, 'italic', 'bold')
        turtle.write(' Compare:          1 \n Count Column:     2 \n Count Record:     3 (Not Release Yet) \n Delete Column:    4 \n Merge File:       5 (Not Release Yet) \n Sort and Compare: 6 \n Sort:             7',
                     font=style, align='right')

        select_function = int(turtle.numinput(
            "Please Select A Function", "Function No."))

        # Function 1: Compare
        # Function 2: Count Column
        # Function 3: Count Record (Not Release Yet)
        # Function 4: Delete Column
        # Function 5: Merge File (Not Release Yet)
        # Function 6: Sort and Compare
        # Function 7: Sort

        if select_function == 1:
            print('Launch Program 1')
            count_object = compre_file.CompareFunction()
            count_object.Run()
        elif select_function == 2:
            print('Launch Program 2')
            count_object = count_column.CountColumnFunction()
            count_object.Run()
        # elif select_function == 3:
        #     print('Launch Program 3')
        elif select_function == 4:
            print('Launch Program 4')
            count_object = delete_column.DeleteFunction()
            count_object.Run()
        # elif select_function == 5:
        #     print('Launch Program 5')
        elif select_function == 6:
            print('Launch Program 6')
            count_object = sort_and_compare.SortAndCompareFunction()
            count_object.Run()
        elif select_function == 7:
            print('Launch Program 7')
            count_object = sort_file.SortFunction()
            count_object.Run()
        else:
            print('Exit The Program')
