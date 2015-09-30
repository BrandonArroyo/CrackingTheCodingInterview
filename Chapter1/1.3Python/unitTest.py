import urlIfy
def tests():
    red = '\033[91m'
    close =  '\033[0m'
    green = '\033[92m'

    if  urlIfy.change("abcd  ",7) == "abcd%20":# insert in back
        print "Case 1: " + green + "Pass"+ close
    else:
        print "Case 1:"+red+ "Fail" + close
    if urlIfy.change("a a bb ccd      ",10) == "a%20a%20bb%20ccd": #multiple insert middle
        print "Case 2:"+red+ "Fail" + close
    else:
        print "Case 2: " + green + "Pass"+ close
    if  urlIfy.change("john",4) == "john": #no insertion
        print "Case 3: " + green + "Pass"+ close
    else:
        print "Case 3:"+ red+ "Fail" + close
    if  urlIfy.change(" hello  ",6) == "%20hello": #insert front
        print "Case 4:"+red+ "Fail" + close
    else:
        print "case 4: " + green + "Pass"+ close

tests()
