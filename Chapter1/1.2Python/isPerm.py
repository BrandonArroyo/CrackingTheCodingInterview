
def isPerm(s1,s2):
    if len(s1) != len(s2): # make sure same length
        return False
    if ''.join(sorted(s1)) == ''.join(sorted(s2)): #sorts then tests the sorted strings
        return True
    else:
        return False
