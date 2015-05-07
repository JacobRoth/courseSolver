import lxml.html
from course import *

MINUTES_IN_WEEK = 10080 

def findCourseTable(tree):
    '''searches through the course tree to find the table that holds
    all the courses'''
    def isWhatWeSeek(tree): # describes if an html tree object is the one we want
        if tree.tag == 'tbody':
            if tree.attrib.has_key('class'):
                if tree.attrib['class']=='gbody':
                    return True
        return False

    if isWhatWeSeek(tree):
        return tree
    else:
        recursionResults = map(findCourseTable,tree)
        for item in recursionResults:
            if item != False:
                return item
        return False

def everyOther(listLike): 
    '''takes every other object from a list or other iterable thing. 
    [0], [2], [4], etc. This is necessary to get the courses 
    out of the course table, because only every other element in the 
    table is a course (the others are blank). '''
    return [listLike[i] for i in filter(lambda x:x%2==0, range(len(listLike)))]

f = open("everyCourse_fall15.htm")
courseTree = lxml.html.fromstring(f.read())
f.close()

sections = everyOther(findCourseTable(courseTree))
sectionObjs = list(map(Section.fromElementObject,sections))
coursesAsLists = segment(sectionObjs,lambda obj:obj.code.split("-")[0]) # we want to take everything before the course code 
courses = [ Course(segment,segment[0].name,segment[0].code.split("-")[0]) for segment in coursesAsLists ] # we take segment[0] as the first section and use its name and code to construct the Course.
