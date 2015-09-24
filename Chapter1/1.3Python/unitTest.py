import urlIfy
def tests():
    red = '\033[91m'
    close =  '\033[0m'
    green = '\033[92m'

    if  urlIfy.change("abcd") == "abcd":
        print "Case 1: " + green + "Pass"+ close
    else:
        print "Case 1:"+red+ "Fail" + close
    if urlIfy.change("aabbccdd") == "ads":
        print "Case 2:"+red+ "Fail" + close
    else:
        print "Case 2: " + green + "Pass"+ close
    if  urlIfy.change("john") == "john":
        print "Case 3: " + green + "Pass"+ close
    else:
        print "Case 3:"+ red+ "Fail" + close
    if  urlIfy.change("a") == "bob":
        print "Case 4:"+red+ "Fail" + close
    else:
        print "case 4: " + green + "Pass"+ close

tests()
