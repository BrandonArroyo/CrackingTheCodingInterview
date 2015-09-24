
#Implement an algorithm to determine if a string has all unique characters?
def isUnique(s):
    if len(s) > 128: # if size is smaller than all possible letters then false
        return False
    #possible assuming that all the characters are 128
    array = [-1]* 128 # all possible places
    for i in s:
        if array[ord(i)] != -1:
            return False
        else:
            array[ord(i)] = i
    return True
