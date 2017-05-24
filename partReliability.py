import numpy as np
from scipy.stats import *

class PARTANALYSIS:

    def __init__( self ):

        self.mttf = None
        self.failRate = None
        self.beta = None       # indicates the bathtub curve region in weibull

    # Years
    def convertToRate(self, mttf):

        # Failure Rate = 1 / MTTF
        return ( 1 / mttf)

    def calcReliability(self, years):

        return years * self.convertToRate( self.mttf )
