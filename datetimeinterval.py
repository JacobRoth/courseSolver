import functools

class DateTime():
    '''just a container class to hold all of the parts'''
    def __init__(self,day,hour,pm,minute):#pm is a boolean value 
        self.day = day
        self.hour = hour
        self.pm = pm
        self.minute=minute

    def asMinute(self): 
        '''translates a day, hour, am/pm and minute date into a minute of week
        Ensure that the day string is valid - an invalid day like "U" or "MWF"
        will crash the program.'''
        dayNumber = {'M':0,'T':1,'W':2,'R':3,'F':4,'S':5,'U':6}
        if self.hour == 12:
            realHour = 0 # to handle the fact that 12:30 after noon is 12:30PM not AM (such a dumb system)
        else: 
            realHour = self.hour
        if self.pm:
            realHour += 12 # put it in 24 hour time
        
        return 24*60*dayNumber[self.day] + 60*realHour + self.minute # that should return minute of week.

class TimeInterval():
    '''represents an interval in time'''
    def __init__(self,dt1,dt2):
        '''dt1 must come before dt2! otherwise you get nonsensical results.'''
        self.dt1 = dt1
        self.dt2 = dt2
    def isActive(self,minuteOfWeek):
        return (self.dt1.asMinute() < minuteOfWeek) and (minuteOfWeek < self.dt2.asMinute())

class NullInterval(TimeInterval):
    '''dummy inteval that isn't located anywhere in time and is always not active'''
    def __init__(self):
        pass
    def isActive(self,minuteOfWeek):
        return False

def decomposeCourseTimeString(courseTimeString):
    ''' returns a list of intervals corresponding to this time string'''
    try:
    
        daysIndex = courseTimeString.index('\xa0')    
        days = courseTimeString[0:daysIndex]
        
        cts2=courseTimeString[daysIndex+1:] # days text chopped off

        startHourIndex = cts2.index(":")
        startHour = int(cts2[0:startHourIndex])

        cts3 = cts2[startHourIndex+1:]
        startMinute = int(cts3[0:1])
        cts4 = cts3[2:]
        if cts4[0:1] == 'AM':
            startPM = False
        elif cts4[0:1] == 'PM':
            startPM = True
        else:
            startPM = 'SAME' # copy in endPM as this value

        theRest = cts4.split()
        endTime = theRest[1]
        endTimeDecomposed = endTime.split(":")
        endHour = int(endTimeDecomposed[0])
        endMinute = int(endTimeDecomposed[1])

        if theRest[2][0:1] == 'AM':
            endPM = False
        else:
            endPM = True

        if startPM == 'SAME':
            startPM = endPM
        #print(days,startHour,startMinute,startPM,endHour,endMinute,endPM)
        return [ TimeInterval(DateTime(day,startHour,startPM,startMinute),DateTime(day,endHour,endPM,endMinute)) for day in days] # return a list of intervals that represent equivalent time intervals but on different days (i.e. one each for Monday, Wednesday, Friday from 3:00PM to 6:00 PM
    except: 
        # If that above parsing code fails for any reason, this must be one of those courses that doesn't meet regularly. It won't factor into the schedule.
        return [ NullInterval() ] 


