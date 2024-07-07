# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skusChars = sorted(list(skus))
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    counts = {(x, 0) for x in alpha}
    prices = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40, 'F':10, 'G': 20, 'H':10, 'I':35, 'J':60, 'K':80, 'L':90, 'M':15, 'N':40, 'O':10, 'P':50, 'Q':30, 'R':50, 'S':30, 'T':20, 'U':40, 'V':50, 'W':20, 'X':90, 'Y':10, 'Z':50}

    for s in skusChars:
        if s in alpha:
            counts[s] += 1
        else:
            return -1

    result = 0

    if counts['E'] > 1:
        if counts['E'] // 2 >= counts['B']:
            counts['B'] = 0
        else:
            counts['B'] -= counts['E'] // 2
    
    if counts['A'] // 5 > 0:
        result = 200 * (counts['A'] // 5)
        counts['A'] %= 5
    
    result += 50 * (counts['A'] % 3) + 130 * (counts['A'] // 3)
    result += 30 * (counts['B'] % 2) + 45 * (counts['B'] // 2)
    result += 20 * counts['C']
    result += 15 * counts['D']
    result += 40 * counts['E']
    result += 10 * (counts['F'] % 3) + 20 * (counts['F'] // 3)

    for s in alpha:
        result += prices[s] * counts[s]
    
    return result
