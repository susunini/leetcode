def shorten_string(input_str):
    """ Shorter a String.
    每个字母最多连续出现两次，超过两次的就不保留了
    e.g. aaabaaccc–> aabaacc
    """
    if not input_str:
        return ''
    result = ''
    cur_letter = input_str[0]; count = 1
    for i in range(1, len(input_str)):
        if input_str[i] == cur_letter:
            count += 1
        if input_str[i] != cur_letter or i == len(input_str)-1: # Wrong: else
            result += cur_letter*min(2, count)
            cur_letter = input_str[i]; count = 1
    return result

assert(shorten_string('aaabaadccc') == 'aabaadcc')
assert(shorten_string('') == '')
