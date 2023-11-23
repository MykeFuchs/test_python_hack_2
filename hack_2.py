"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(result):
    return solution(result)

def solution(word):
    vocals = "aeiou"
    answer = ""
    for letter in word:
        if letter not in vocals:
            answer += letter
    return answer