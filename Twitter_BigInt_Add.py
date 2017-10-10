def add(str1, str2):
    i = len(str1)-1
    j = len(str2)-1
    carry = 0
    result = ''
    while i >= 0 or j >= 0 or carry:
        sum = 0
        sum += int(str1[i]) if i >= 0 else 0
        sum += int(str2[j]) if j >= 0 else 0
        sum += carry
        result = str(sum%10)+result
        carry = sum/10
        i -= 1; j -= 1
    return result

assert(add('0', '123') == '123')
assert(add('123', '1234') == '1357')
assert(add('123', '1234') == '1357')
assert(add('1234', '123') == '1357')
assert(add('999', '9999') == '10998')

