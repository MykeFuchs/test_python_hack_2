"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(result):
    return solution(result)

def solution(word):
    if "a" in word:
       word = word.replace("a","@")
    if "e" in word:
        word = word.replace("e","3")
    if "i" in word:
        word = word.replace("i","¡")
    if "o" in word:
        word = word.replace("o","0")
    if "u" in word:
        word = word.replace("u","v")
    if "q" in word:
        word = word.replace("q","Q")
    if "x" in word:
        word = word.replace("x","X")
    if "f" in word:
        word = word.replace("f","F")
    if "n" in word:
        word = word.replace("n","N")
    if "b" in word:
        word = word.replace("b","B")
    return word