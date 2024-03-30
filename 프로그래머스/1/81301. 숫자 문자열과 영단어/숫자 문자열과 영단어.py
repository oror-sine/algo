_num_strings = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

dictionary = {
    string[:2]: (str(digit), len(string))
    for digit, string
    in enumerate(_num_strings)    
}

def solution(s):
    answer = []
    index = 0
    while index < len(s):
        digit, length = dictionary.get(s[index:index+2], (s[index],1))
        answer.append(digit)
        index += length
        
    return int(''.join(answer))