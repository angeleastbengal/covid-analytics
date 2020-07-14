#---------------------------------Student ID: 31131867---------------------------------------
#---------------------------------Name: Angel Das--------------------------------------------
#---------------------------------Create Date: 05-06-2020------------------------------------
#---------------------------------Last Modified: 07-06-2020----------------------------------
#---------------------------------Note: Version Control is used to save files----------------

from a2_31131867_task2 import *
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# import statement to make use of functions/classes from earlier task(s).

# global counter
# counter=1

def visual_curve(days, meeting_probability, patient_zero_health):

    # global counter

    list_contagious=run_simulation(days, meeting_probability, patient_zero_health)

    #-----------------------List is converted into a data frame-----------------------------------
    list_contagious = pd.DataFrame(list_contagious) #---------------Converting list to a dataframe-----------
    list_contagious.rename(columns={0: 'Infected Patient Count'}, inplace=True)

    #----------------------Adding columns for days------------------------------------------------
    list_contagious['Days'] = np.arange(len(list_contagious)) + 1
    list_contagious.set_index('Days', inplace=True)

    list_contagious.plot(kind='line', figsize=(10, 6)) #-----------Figure size
    plt.title('Infected patient counts across days') #-------------Title
    plt.xlabel('Day') #--------Label on X axis
    plt.ylabel('#Contagious Patients') #-------------------Label on Y axis
    # sav="Figure - "+str(counter)
    plt.savefig("Figure - Simulation") #-----------------Saving the plot
    # counter+=1

if __name__ == '__main__':

    #----------------------Asking user for number of days, meeting probability and health-------------------------------
    #----------------------Note checks for these variables are done in task2 already------------------------------------

    day=int(input("Enter the number of days to run the simulation:"))
    prob=float(input("Enter the meeting probability:"))
    health=float(input("Enter the initial health of patient zero:"))
    for i in range(0,20):
        visual_curve(day,prob,health)


