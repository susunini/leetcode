import collections

def is_anagram_pandindrome(input_str):
    """ Check if any anagram of input string is an anagram. 
    https://instant.1point3acres.com/thread/256142/post/2353850
    """
    counter = collections.Counter(input_str)
    num_of_odd = 0
    for letter, count in counter.items():
        if count%2:
            num_of_odd += 1
        if num_of_odd > 1:
            return False
    return True

assert(is_anagram_pandindrome('abcb') == False)
assert(is_anagram_pandindrome('abcab') == True)
assert(is_anagram_pandindrome('abcb') == False)
assert(is_anagram_pandindrome('  ') == True)
