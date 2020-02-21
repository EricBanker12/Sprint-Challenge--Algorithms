'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    """Returns count of 'th' in a string. Case-sensitive."""
    # non-recursive:
    # return word.count('th')
    
    # TBC
    if len(word) < 2:
        return 0
    elif word[0:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        return count_th(word[1:])