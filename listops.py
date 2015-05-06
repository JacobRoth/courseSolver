def segment(listOfObjects,attribLambda):
    '''segments a list of objects into multiple lists, each object in a given list having the same value of attribLambda(obj)'''
    attribValues = map(attribLambda,listOfObjects)
    attribValuesSet = set(attribValues) # makes it into a set, sort of like a list that's unordered and with no repeats.
    return [ [ obj for obj in listOfObjects if attribLambda(obj) == attribValue ]  for attribValue in attribValuesSet ] 

