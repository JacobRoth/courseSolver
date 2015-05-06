import functools,itertools
from datetimeinterval import * #code i wrote to handle course time strings. 
from listops import *


class Section():
    def __init__(self,name,code,intervalsList):
        self.name = name 
        self.intervalsList = intervalsList
        self.code = code

    @classmethod # some weird python voodoo i found on stackoverflow. It lets me make an alternate constructor.
    def fromElementObject(cls,elementObject): # i think cls is like self but it represents this class not this instance
        '''constuct a Course object from the lxml Element Object representing that course'''

        timeStrings = [elementObject[6][0][0][iii].text for iii in range(len(elementObject[6][0][0]))]
        intervalsList = sum(map(decomposeCourseTimeString,timeStrings),[]) # each decompose returns a list of intervals. We're going to get multiple of these lists and we want to concatenate them all togetherer. sum( listOfLists, []) concatenates the way we want.
        return cls(elementObject[2].text,elementObject[1][0].text,intervalsList)
    def isActive(self,minuteOfWeek):
        return any( map( lambda interval: interval.isActive(minuteOfWeek), self.intervalsList)) 

class Course():
    def __init__(self,sections,name):
        self.sections = sections
        self.name = name
    def isRepresented(self,schedule):
        for section in self.sections:
            if section in schedule:
                return True
        return False
    
def activityFunction(schedule):
    '''takes a schedule, returns a function on one variable (t) that is the square-wave representation of that schedule. If the activity function ever
    goes over 1, it is a conflicting schedule'''
    return (lambda t: sum([section.isActive(t) for section in schedule]))

def schedules(listOfCourses):
    '''if you have a list of courses, returns a list of schedules (schedule is a list of sections) that contain all those courses'''
    
    allPossibleSchedules = list(itertools.product(*[course.sections for course in listOfCourses]))
    scheduleIsNonconflicting = lambda schedule: max(map(activityFunction(schedule),range(0,MINUTES_IN_WEEK))) <= 1
    
    nonConflictingSchedules = list(filter(scheduleIsNonconflicting  ,allPossibleSchedules))

    # I just don't like how python3 forces you to cast everything to list to make those functional constructs work correctly. Like seriously, those above
    # two lines just sort of don't work if the list() operations aren't there. Or maybe I'm doing this all wrong.

    # sanity testing part
    for schedule in nonConflictingSchedules:
        for course in listOfCourses:
            assert(course.isRepresented(schedule))
    return nonConflictingSchedules

