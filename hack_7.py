"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
"""

def fn_hack_7(result):
    return solution(result);

def solution(arrayElements):
    answer = []
    flag = True
    if(len(arrayElements) != 0 and arrayElements != [0]):
        for k in range(1,len(arrayElements)+1):
            if(flag):
                answer.append(str(k))
                flag = False
            else:
                answer.append(k)
                flag = True
    else:
        answer = [0]
    return answer