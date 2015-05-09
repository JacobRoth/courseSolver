import matplotlib.pyplot as plt
from course import *

def visualize(schedule):
    theWeek = range(0,MINUTES_IN_WEEK)
    plt.plot( list(theWeek) , list(map(activityFunction(schedule),theWeek)))
    plt.show()
    plt.clf() # clear figure for next run of visualize
    plt.cla() # clear axes
