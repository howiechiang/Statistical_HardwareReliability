import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from testAcceleratedLife import TESTACCELERATEDLIFE
import testVariables as c
from tkinter import *


class TESTLIFEDATA:

    def __init__( self ):

        self.testUnits = None
        self.testMedianTimeInterval = None
        self.testCumulativeFailures = None
        self.cumulativeProbability = None


    def calcCumProbability(self):

        self.cumulativeProbability = [(100 * (x - 0.3) / (self.testUnits + 0.4)) for x in self.testCumulativeFailures]


    def collectData(self):

        def insertLabels():
            for i in range(len(cols)):
                e = Entry(relief="ridge", font=("Arial", 8, "bold"),
                          bg="#ffffff000", fg="#000000fff",
                          readonlybackground="#ffffff000",
                          justify='center', width=22)
                e.grid(row=0, column=i)
                e.insert(END, cols[i])
                e.config(state="readonly")

            for i in range(len(rows)):
                e = Entry(relief="ridge", font=("Arial", 8, "bold italic"),
                          bg="#ffffff000", fg="#000000fff",
                          readonlybackground="#ffffff000",
                          justify='center', width=22)
                e.grid(row=i + 1, column=0)
                e.insert(END, rows[i])
                e.config(state="readonly")

        def insertCells():
            row = []
            for i in range(1, len(rows) + 1):
                col = []
                for j in range(1, len(cols)):
                    e = Entry(relief="ridge", font=("Arial", 8),
                              bg="#ddddddddd", fg="#000000000",
                              justify='center', width=22)
                    e.grid(row=i, column=j, sticky=NSEW)
                    e.insert(END, '')
                    col.append(e)
                row.append(col)
            return row

        eTable = Tk()

        cols = ['', 'Median Time Interval', 'Failures Per Interval']
        rows = np.arange(1, 10, 1)

        eTable.title('Data Entry')
        eTable.config(padx='3.0m', pady='3.0m')
        eTable.grid()
        insertLabels()
        gridDict = insertCells()

        global testData
        testData = np.zeros(shape=(len(gridDict), len(gridDict[0])))

        def onPress():

            for i in range(len(gridDict)):
                for j in range(len(gridDict[0])):
                    if gridDict[i][j].get() != '':
                        testData[i][j] = (gridDict[i][j].get())

            # Check that everything is inputted correctly
            for i in range(len(testData)):
                if testData[i][0] == 0 and testData[i][0] != testData[i][1]:
                    print('Please fix data, there are blank sections...')

            print('If the table looks correct, please close the Data Entry Table')

        Button(text='Fetch', justify='center', command=onPress).grid()
        mainloop()

    def setData(self):


        self.testMedianTimeInterval = [s for s in testData[:,0] if s!= 0]
        self.testCumulativeFailures = [s for s in testData[:,1] if s!= 0]
        self.testCumulativeFailures = np.cumsum(self.testCumulativeFailures)