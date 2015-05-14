import matplotlib.pyplot as plt
from course import *

def visualize(schedule):
    theWeek = range(0,MINUTES_IN_WEEK)
    plt.plot( list(theWeek) , list(map(activityFunction(schedule),theWeek)))
    plt.show()
    plt.clf() # clear figure for next run of visualize
    plt.cla() # clear axes

def printSchedule(schedule):
    template = "{0:14} | {1:40} | {2:20}"
    for section in schedule:
        if len(section.timeStrings)== 0: # section has no timestrings associated with it. (Wont happen, but I'd like to cover this case anyway)
            print(template.format(section.code, section.name,''))
        else:
            print(template.format(section.code, section.name,section.timeStrings[0])) # print the zeroth time string 
            if len(section.timeStrings) >= 2: # if there are two or more time strings, we should print those others.
                for timeString in section.timeStrings[1:]:
                    print(template.format("", "", timeString)) # print the zeroth time string 
        print("") # pad space for next section

def treeRender(listsOfCourses):
    for iii in range(len(listsOfCourses)):
        print("---Block ",iii)
        for jjj in range(len(listsOfCourses[iii])):
            print("   |-{0:3}: ".format(str(jjj)),listsOfCourses[iii][jjj])
