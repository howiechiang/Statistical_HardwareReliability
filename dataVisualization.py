import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from testAcceleratedLife import TESTACCELERATEDLIFE
from testLifeData import TESTLIFEDATA
import testVariables as c



def plotReliabilityAccelLife(testSetup):

    if not isinstance(testSetup, TESTACCELERATEDLIFE):
        raise TypeError("Please pass a test setup (CLASS TESTPARAMETERS)")

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.4)
    tMax = c.productLife
    t = np.linspace(0, tMax, 100)
    r = np.exp(-testSetup.failRate * t)

    l, = plt.plot(t, r, lw=2, color='#FF0000')
    plt.axis([0, tMax, min(r)-.01, max(r)])
    # l, = plt.semilogy(t, r, lw=2, color='#FF0000')
    # plt.axis([0, tMax, 0.5, max(r)])
    # plt.yscale('symlog')


    plt.xlabel('Use Time (Hours)', fontweight='bold')
    plt.ylabel('Reliability', fontweight='bold')
    plt.title('Reliability Over Time', fontweight='bold')
    ax.grid(True)
    ax.set_facecolor('#CEE3F6')

    # Adjustable Content
    axcolor = '#F5F6CE'
    ax_testUnits = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)
    ax_testFailures = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
    ax_testDuration = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
    ax_testConfidenceLevel = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)

    s_testUnits = Slider(ax_testUnits, 'Test Units', 1, 800, valinit=testSetup.testUnits, valfmt='%1.0f')
    s_testFailures = Slider(ax_testFailures, 'Test Failures', 0, 100, valinit=testSetup.testFailures, valfmt='%1.0f')
    s_testDuration = Slider(ax_testDuration, 'Test Duration(Hrs)', 1, 800, valinit=testSetup.testDuration, valfmt='%1.0f')
    s_testConfidenceLevel = Slider(ax_testConfidenceLevel, 'Confidence Level', 0, 1, valinit=testSetup.testConfidenceLevel)

    def update(val):
        testSetup.setVariables(s_testUnits.val, s_testDuration.val, s_testFailures.val, s_testConfidenceLevel.val)
        testSetup.calcFailRate()

        r = np.exp(-testSetup.failRate * t)
        l.set_ydata(r)
        fig.canvas.draw_idle()
        #plt.axis([0, tMax, min(r) - .01, max(r)])


    s_testConfidenceLevel.on_changed(update)
    s_testDuration.on_changed(update)
    s_testFailures.on_changed(update)
    s_testUnits.on_changed(update)

    plt.show()

def plotWeibull(testLifeData):

    if not isinstance(testLifeData, TESTLIFEDATA):
        raise TypeError("Please pass a test setup (CLASS TESTLIFEDATA)")

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    t = testLifeData.testMedianTimeInterval
    p = testLifeData.cumulativeProbability

    # Calculate Polynomial
    z = np.polyfit(t,p, 2)
    f = np.poly1d(z)

    #Calculate new x's and y's
    t_new = np.linspace(min(t), max(t), 50)
    p_new = f(t_new)


    plt.plot(t, p, 'o-', color='#0000FF')
    plt.plot(t_new, p_new, '-', color='#3ADF00')
    plt.axis([0, max(t)*1.15, 0, 100])
    ax.set_xticks(np.arange(0, max(t)*1.15, t[0]/10), minor = True)
    ax.set_yticks(np.arange(0, 100, 5), minor = True)
    ax.grid(which='minor', alpha=0.2)

    plt.xlabel('Use Time (Hours)')
    plt.ylabel('Reliability')
    plt.title('Reliability Over Time')
    plt.grid(True)

    plt.xlabel('Time (Hours)', fontweight='bold')
    plt.ylabel('Cumulative Probability', fontweight='bold')
    plt.title('Weibull MLE Probability (CDF) Plot and Data FIT \n (Fit=Green, Data=Blue)',
              fontsize=14, fontweight='bold')
    plt.grid(True)
    # ax.set_facecolor('#CEE3F6')

    plt.show()