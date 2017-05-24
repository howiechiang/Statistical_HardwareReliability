import numpy as np
from scipy.stats import chi2
from math import *
import scipy.constants
import testVariables as c

class TESTACCELERATEDLIFE:

    def __init__( self ):

        # Variables
        self.testUnits = None               # Units
        self.testDuration = None            # Hours
        self.testFailures = None            # Units
        self.testConfidenceLevel = None    # percentage

        #Checks
        self.paramTempExist = False
        self.paramHumidExist = False
        self.paramVibExist = False

        # Calculated
        self.accelFactor = None
        self.failRate = None

    def setVariables(self, tUnits, tDuration, tFailures, CL):

        self.testUnits = tUnits
        self.testDuration = tDuration
        self.testFailures = tFailures
        self.testConfidenceLevel = CL

    # This calculates the upper range of fail rate
    # Fail rate is per hour (or whatever the units of time test duration was inputted at)
    def calcFailRate(self):

        # chi2.ppf is the 'inverse right-tailed chi-squared'
        self.failRate = chi2.ppf(self.testConfidenceLevel, (2 * self.testFailures) + 2) \
                        / (2 * self.accelFactor * self.testDuration * self.testUnits)

        return self.failRate

    # This returns the reliability of a product after x hours
    # @param tUsed = after x hours
    def calcReliabilityOverTime(self, tUsed=c.productLife):

        self.calcFailRate()     # This is done to include any changes to test parameters
        temp = exp(-1 * self.failRate * tUsed)
        print('Reliability after ', tUsed, ' hours is ', temp)

        return temp

    def reqAccelFactor(self):

        if self.testDuration == None:
            return "No 'testDuration' variable set, please set and retry"

        else:
            return  c.productLife / self.testDuration

    # Prints all Parameters of the Test
    def printParams(self):

        # Basic Test Set up
        print('Test Units: ', self.testUnits)
        print('Test Failures: ', self.testFailures)
        print('Test Duration: ', self.testDuration)

        # Stressed Parameters
        print('Stressed Environment Settings: ', end='')
        if self.paramTempExist == True:
            print('Temperature', end=', ')
        if self.paramHumidExist == True:
            print('Humidity', end=', ')
        if self.paramVibExist == True:
            print('Vibration', end=', ')
        print()

        # Statistical Analysis
        print('Acceleration Factor: ', self.accelFactor)
        print('Accelerated Test Time: ', self.testDuration * self.accelFactor)
        print('Failure Rate [per hour]: ', self.failRate)


    # Utilizes the Linear Expression for Arrhenius Model
    # @param tUse = Product use temperature in Kelvins
    # @param tStress = Product stress temperature in Kelvins
    def setTempAccelFactor(self, tUse, tStress):

        if self.paramTempExist == False:
            self.accelFactor = exp((tUse ** -1 - tStress ** -1) * c.actEnergy_general / c.cBoltzmann)
            self.paramTempExist = True

        elif self.paramTempExist == True:
            print('Test parameters and acceleration factor for vibration is already set...')
            print("Use 'ClearAccelFactor()' to reset...")

    # Utilizes the Peck Model
    # @param rhUse = Product use humidity in Kelvins
    # @param rhStress = Product stress humidity in Kelvins
    def setHumidAccelFactor1(self, rhUse, rhStress):

        if self.paramHumidExist == False:
            self.accelFactor = (rhStress / rhUse) ** c.cPeck
            self.paramHumidExist = True

        elif self.paramHumidExist == True:
            print('Test parameters and acceleration factor for vibration is already set...')
            print("Use 'ClearAccelFactor()' to reset...")

    # Utilizes Simplified Model
    # @param dtUse = delta of use temperature
    # @param dtStress = delta of stress temperature
    def setTempCycleAccelFactor1(self, dtUse, dtStress):

        if self.paramTempExist == False:
            self.accelFactor = (dtStress / dtUse) ** c.cTempCycleExp
            self.paramTempExist = True

        elif self.paramTempExist == True:
            print('Test parameters and acceleration factor for vibration is already set...')
            print("Use 'ClearAccelFactor()' to reset...")

    # Utilizes modified frequency effect Coffin Manson Model
    # @param dtUse = delta of use temperature
    # @param dtStress = delta of stress temperature
    # @param fUse = frequency when used
    # @param fStress = frequency when stressed
    # @param tUse = temperature in use
    # @param tStress = max temperature in stress

    def setTempCycleAccelFactor2(self, dtUse, dtStress, fUse, fStress, tUse, tStress):

        if self.paramTempExist == False:
            self.accelFactor = (dtStress / dtUse) ** c.cTempCycleExp * \
                               (fUse / fStress) ** 0.33 * \
                               exp((tUse ** -1 - tStress ** -1) * c.actEnergy_general / c.cBoltzmann)
            self.paramTempExist = True

        elif self.paramTempExist == True:
            print('Test parameters and acceleration factor for vibration is already set...')
            print("Use 'ClearAccelFactor()' to reset...")


    # Utilizes vibration acceleration model
    # @param tUse = Vibration duration during use
    # @param tStress = Vibration duration stressed in lab

    def setVibAccelFactor1(self, tUse, tStress):

        if self.paramVibExist == False:
            self.accelFactor = tUse / tStress
            self.paramVibExist = True

        elif self.paramVibExist == True:
            print('Test parameters and acceleration factor for vibration is already set...')
            print("Use 'ClearAccelFactor()' to reset...")

    # Utilizes vibration acceleration model
    # @param wUse = Random Vibe PSD in use (G**2 / Hz)
    # @param wStress = Random Vibe PSD in stress (G**2 / Hz)

    def setVibAccelFactor2(self, wUse, wStress):

        if self.paramVibExist == False:
            self.accelFactor = (wStress / wUse) ** (c.cFatigueParam / 2)
            self.paramVibExist = True

        elif self.paramVibExist == True:
            print('Test parameters and acceleration factor for vibration is already set...')
            print("Use 'ClearAccelFactor()' to reset...")

    # Utilizes vibration acceleration model
    # @param gUse = Sinusoid vibration level or rms content in use
    # @param gStress = Sinusoid vibration level or rms content in stress

    def setVibAccelFactor3(self, gUse, gStress):

        if self.paramVibExist == False:
            self.accelFactor = (gStress / gUse) ** c.cFatigueParam
            self.paramVibExist = True

        elif self.paramVibExist == True:
            print('Test parameters and acceleration factor for vibration is already set...')
            print("Use 'ClearAccelFactor()' to reset...")

    def clearAccelFactor(self):

        self.accelFactor = None

        self.paramTempExist = False
        self.paramHumidExist = False
        self.paramVibExist = False

