from math import *
import numpy as np



# enable subsystems and recalculations when subsystems are introduced.


class SYSTEMFAILUREANALYSIS:

    def __init__( self ):

        self.rateFailures = np.array([])

    def rateSystemFailure( self ):

        return 1 / sum( 1 / self.rateFailures )


    def solveParallelRequired( self, partMTBF, reqMTBF):

        curMTBF = partMTBF
        reqParallel = 1

        while curMTBF < reqMTBF:

            reqParallel += 1
            curMTBF = reqParallel * partMTBF - 1 / ( reqParallel * (1 / partMTBF))

        return reqParallel