from math import *
import numpy as np
from systemAnalysis import SYSTEMFAILUREANALYSIS
from partReliability import PARTANALYSIS
from testAcceleratedLife import TESTACCELERATEDLIFE
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from dataVisualization import *


accLife = TESTACCELERATEDLIFE()
accLife.setVariables(25, 170, 0, 0.8)
accLife.setTempAccelFactor(c.temp_NormalUse, c.temp_NormalUse + 50)
accLife.calcFailRate()
plotReliabilityAccelLife(accLife)

