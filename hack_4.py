"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(result):
    return solution(result) 

def solution(word):
    word = word if len(word) <= 3 else word[1:-1]
    return word