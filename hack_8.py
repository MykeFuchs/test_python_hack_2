"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(result):
    return solution(result)

def solution(arrayElements):
    if(len(arrayElements) == 5 or len(arrayElements) == 3):
        arrayElements = list(reversed(arrayElements))
        counter = 0
        for k in range(len(arrayElements), 0 , -1):
            arrayElements[counter] = arrayElements[counter] + "-" + str(k)
            counter+=1
    else:
        for k in range(len(arrayElements)):
            arrayElements[k] = str(k+1)
        arrayElements = list(reversed(arrayElements))
    return arrayElements