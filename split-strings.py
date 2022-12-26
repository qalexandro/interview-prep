'''
Complete the solution so that it splits the string into pairs of two characters. 
If the string contains an odd number of characters then it should replace the missing 
second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']

'''

def solution(s):
    n = 2
    s = s + "_" if len(s) % 2 == 1 else s
    return [s[i:i+n] for i in range(0, len(s), n)]


# with regular expression
import re
def solution1(s):
    return re.findall(".{2}", s + "_")

print(solution("acdefecevev"))
print(solution1("acdefecevev"))