#calculate the number of steps a child can run up a stair case
#given 1 step, 2 step, 3 steps 




def stairsMemEff(n):
    if n <= 0:
        return 0 
    loPaths = [1, 2, 4]

    for i in range(3, n):
        toAdd = loPaths[(i - 1)%3] + loPaths[(i - 2)%3] + loPaths[(i - 3)%3]
        loPaths[0] = loPaths[1]
        loPaths[1] = loPaths[2]
        loPaths[2] = toAdd

    if n < 3:
        return loPaths[n - 1] 
    return loPaths[2]

def stairs(n):
    if n <= 0:
        return 0 
    loPaths = [1, 2, 4]

    for i in range(3, n):
        toAdd = loPaths[i - 1] + loPaths[i - 2] + loPaths[i - 3]
        loPaths.append(toAdd) 
    return loPaths[n - 1] 

def stairsRec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else: 
        return stairsRec(n - 1) + stairsRec(n - 2) + stairsRec(n - 3)

assert 0 == stairs(0)
assert 1 == stairs(1)
assert 2 == stairs(2)
assert 4 == stairs(3)
assert 7  == stairs(4)
assert 13 == stairs(5)

assert stairsRec(5) == stairs(5)
assert stairsMemEff(5) == stairs(5) 
assert stairsMemEff(1) == stairs(1)
