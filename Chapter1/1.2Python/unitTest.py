import isPerm
def tests():
    red = '\033[91m'
    close =  '\033[0m'
    green = '\033[92m'

    if  isPerm.isPerm("cat","cat"):
        print "Case 1: " + green + "Pass"+ close
    else:
        print "Case 1: "+red+ "Fail" + close
    if isPerm.isPerm("dog","cat"):
        print "Case 2:"+red+ "Fail" + close
    else:
        print "Case 2: " + green + "Pass"+ close
    if  isPerm.isPerm("abcd","dcab"):
        print "Case 3: " + green + "Pass"+ close
    else:
        print "Case 3: "+ red+ "Fail" + close
    if  isPerm.isPerm("defa","def"):
        print "Case 4: "+red+ "Fail" + close
    else:
        print "case 4: " + green + "Pass"+ close

tests()
