from math import *
import numpy as np
from systemAnalysis import SYSTEMFAILUREANALYSIS
from partReliability import PARTANALYSIS
from testAcceleratedLife import TESTACCELERATEDLIFE
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from dataVisualization import *
from testLifeData import TESTLIFEDATA

a = TESTLIFEDATA()
a.testUnits = 7     # Total Test units must be put in here....
a.collectData()
a.setData()
a.calcCumProbability()

plotWeibull(a)