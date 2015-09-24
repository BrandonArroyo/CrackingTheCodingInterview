import isUnique
def tests():
    red = '\033[91m'
    close =  '\033[0m'
    green = '\033[92m'

    if  isUnique.isUnique("abcd"):
        print "Case 1: " + green + "Pass"+ close
    else:
        print "Case 1:"+red+ "Fail" + close
    if isUnique.isUnique("aabbccdd"):
        print "Case 2:"+red+ "Fail" + close
    else:
        print "Case 2: " + green + "Pass"+ close
    if  isUnique.isUnique("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"):
        print "Case 3: " + green + "Pass"+ close
    else:
        print "Case 3:"+ red+ "Fail" + close
    if  isUnique.isUnique("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890a"):
        print "Case 4:"+red+ "Fail" + close
    else:
        print "case 4: " + green + "Pass"+ close

tests()
