'''
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
Examples

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
'''

def reverse_words(text):
    #return "  ".join(list(map(lambda str: "".join(reversed(str)), text.split())))
    return " ".join(s[::-1] for s in text.split(" "))

print(reverse_words("The quick brown fox jumps over the lazy dog."))
print(reverse_words("a b c d"))
print(reverse_words("double  spaced  words"))