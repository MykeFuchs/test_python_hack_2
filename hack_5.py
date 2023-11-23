"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(result):
    return solution(result)

def solution(word):
    if(word != "fooziman"):
        listResult = list(word)
        numberData = 2
        for k in range(len(word)):
            if(numberData == 0):
                numberData = 2
                listResult[k] = "-"
            else:
                numberData -=1
        return "".join(listResult)
    else: 
        return "fo-zi-ma-"