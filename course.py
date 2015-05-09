import functools,itertools
from datetimeinterval import * #code i wrote to handle course time strings. 
#from listops import *

MINUTES_IN_WEEK = 7*24*60
class Section():
    def __init__(self,name,code,intervalsList,timeStrings=[]): #
        self.name = name 
        self.intervalsList = intervalsList
        self.code = code
        self.timeStrings=timeStrings

    @classmethod # some weird python voodoo i found on stackoverflow. It lets me make an alternate constructor.
    def fromElementObject(cls,elementObject): # i think cls is like self but it represents this class not this instance
        '''constuct a Course object from the lxml Element Object representing that course'''

        timeStrings = [elementObject[6][0][0][iii].text for iii in range(len(elementObject[6][0][0]))]
        intervalsList = sum(map(decomposeCourseTimeString,timeStrings),[]) # each decompose returns a list of intervals. We're going to get multiple of these lists and we want to concatenate them all togetherer. sum( listOfLists, []) concatenates the way we want.
        return cls(elementObject[2].text,elementObject[1][0].text,intervalsList,timeStrings)

    def isActive(self,minuteOfWeek):
        return any( map( lambda interval: interval.isActive(minuteOfWeek), self.intervalsList)) 

'''class Course():
    def __init__(self,sections,name,code):
        self.sections = sections
        self.name = name
        self.code = code
    def isRepresented(self,schedule):
        for section in self.sections:
            if section in schedule:
                return True
        return False''' # I've decided this Object is unnecessary complexity
    
def activityFunction(schedule):
    '''takes a schedule, returns a function on one variable (t) that is the square-wave representation of that schedule. If the activity function ever
    goes over 1, it is a conflicting schedule'''
    return (lambda t: sum([section.isActive(t) for section in schedule]))

def schedules(listsOfSections):
    '''if you have a list of courses, returns a list of schedules (schedule is a list of sections) that contain all those courses'''
    
    allPossibleSchedules = list(itertools.product(*listsOfSections))
    scheduleIsNonconflicting = lambda schedule: max(map(activityFunction(schedule),range(0,MINUTES_IN_WEEK))) <= 1
    
    nonConflictingSchedules = list(filter(scheduleIsNonconflicting  ,allPossibleSchedules))

    # I just don't like how python3 forces you to cast everything to list to make those functional constructs work correctly. Like seriously, those above
    # two lines just sort of don't work if the list() operations aren't there. Or maybe I'm doing this all wrong.

    # sanity testing part
    for schedule in nonConflictingSchedules:
        for listOfSections in listsOfSections:
            assert(any(map(lambda section: section in listOfSections ,schedule)))

    return nonConflictingSchedules

