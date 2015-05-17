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

def treeRender(blockStructure):
    print(" ")
    for iii in range(len(blockStructure)):
        print("---Block ",iii)
        if len(blockStructure[iii])== 0: #no sections here
            print("   | No sections in this block")
        for jjj in range(len(blockStructure[iii])):
            print("   |-{1:3}: ".format(str(jjj)),blockStructure[iii][jjj])
    print(" ")

def tuiChoice(prompt,optionsList):
    '''loops until you make a valid choice from optionsList. Must be passing in a list of strings for optionsList'''
    assert(all(list(map( lambda x: type(x)==str, optionsList)))) # confirm withe the programmer that it's a list of all strings.
    received = input(prompt) 
    while ( not ( received.strip() in optionsList)):
        print("Bad input, try again")
        received = input(prompt)
    return received.strip() # we use strip to take off any errant spaces.

def main():
    blockStructure = [[]] # reminder - a block structure is a list of lists of sections. course.schedules() takes in a block structure and returns the possible class shedules.
    print("Welcome to the mediocre text interface to Jacob's scheduling algorithm! Enter h for help")
    while (True):
        treeRender(blockStructure)
        cmd = tuiChoice("? ",['h','q','ab','db','as','ds'])
        if cmd == 'h':
            print("All the help text goes here")
        elif cmd == 'q': # quit
            exit()
        elif cmd == 'ab': # add block
            blockStructure.append([])
        elif cmd == 'db': # delete block 
            print("Enter the number of the block you wish to delete, or enter the word \"cancel\".")
            blockToDelete = tuiChoice("Block number: ", list(map(str,range(len(blockStructure))))+["cancel"] )
            if blockToDelete == 'cancel':
                pass  # we aren't taking any action.
            else:
                del blockStructure[int(blockToDelete)] # python is sort of cool like this. We don't do something like myList.removeAtIndex(5), we just do del myList[7]. It's so clean.

        elif cmd == 'as': # add section
            pass # have to program in the search function
        else:
            print("Somehow we hit an unhandled case in the main loop cmd branches! Check your tuiChoice code, programmer!")
            exit()
        
if __name__ == '__main__':
    main()
