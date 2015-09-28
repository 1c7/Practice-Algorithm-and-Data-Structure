# score 44

def solution(X, Y, D):
    # write your code in Python 2.7
    # frog current location X
    # frog want to get to a position greater than or e ual to Y
    # frog always jump a fixed distance D
    distance = Y-X
    jumps = distance / D
    #print distance
    #print jumps
    return jumps+1

