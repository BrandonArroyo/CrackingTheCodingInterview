
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
#Unit tests

# def tests():
#     red = '\033[91m'
#     close =  '\033[0m'
#     green = '\033[92m'
#
#     if isUnique("abcd"):
#         print "Case 1: " + green + "Pass"+ close
#     else:
#         print "Case 1:"+red+ "Fail" + close
#     if isUnique("aabbccdd"):
#         print "Case 2:"+red+ "Fail" + close
#     else:
#         print "Case 2: " + green + "Pass"+ close
#     if isUnique("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"):
#         print "Case 3: " + green + "Pass"+ close
#     else:
#         print "Case 3:"+ red+ "Fail" + close
#     if isUnique("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890a"):
#         print "Case 4:"+red+ "Fail" + close
#     else:
#         print "case 4: " + green + "Pass"+ close
#
# tests()
