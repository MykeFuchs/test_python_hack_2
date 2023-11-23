"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(result):
    return solution(result)

def solution(arrayElements):
    answer = []
    flag = True
    if(len(arrayElements) != 0):
        for k in range(1,len(arrayElements)+1):
            if(flag):
                answer.append(str(k))
                flag = False
            else:
                answer.append("-")
                flag = True
    else:
        answer = ["0"]
    return answer