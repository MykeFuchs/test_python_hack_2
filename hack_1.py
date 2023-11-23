"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(word):
    return solution(word)



def solution(word):
    result = ""
    initialNumber = 2
    if(len(word) > 2):
        for letter in word:
            result += letter
            if(len(result) == initialNumber):
                x = result[-1]
                result = result[:-1] + str(x.upper())
                initialNumber += initialNumber + 1
    else:
        return word

    return result