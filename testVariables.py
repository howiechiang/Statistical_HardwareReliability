import scipy.constants

# Constants
cBoltzmann = scipy.constants.Boltzmann * 6.242e+18  # Convert joules to eV
cPeck = 2.66               # Peck constant, Jedec 122B
cTempCycleExp = 2.0        # Default Qualification Temp Cycle Exponent
cFatigueParam = 7.5        # Fatigue Parameter

# Activation Energy Library
actEnergy_general = 0.7    # eV



# Test Variables
productLife = 5 * 8760      # 5 years * 8760 hours
temp_NormalUse = 25 + 273   # Celcius + Kelvins
dtTemp_NormalUse = 25       # Temperature change ~ guessing between 0-25 C in regular use


rh_NormalUse = 0.3          # Percentage
g_NormalUse = 0             # g^2 / Hz