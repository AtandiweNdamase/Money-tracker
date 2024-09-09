#from  customtkinder import *
#import customtkinder 
from tkinter import ttk
import tkinter as tk
#from moneyTracker import IncomeExpenseTracker
import csv 

class DisplayCSVData:

    def load_file_csv(filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader if row]
        return data
    
    
    def display_incomecsv_data():
        filename = "income.csv"
        data = load_file_csv(filename)

    def display_expenses_data():
        filename = "expenses.csv"
        data = load_file_csv(filename)
 

    print(load_file_csv("income.csv"))
    