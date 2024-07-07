# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skusChars = sorted(list(skus))
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    for s in skusChars:
        if s in ['A','B','C','D','E']:
            counts[s] += 1
        else:
            return -1

    result = 0

    if counts['E'] > 1:
        if counts['E'] // 2 >= counst['B']:
            counts['B'] = 0
        else:
            counts['B'] -= counts['E'] // 2
    
    if counts['A'] // 5 > 0:
        result = 200 * (counts['A'] // 5)
        counts['A'] %= 5
    
    result += 50 * (counts['A'] % 3) + 130 * (counts['A'] // 3)
    result += 30 * (counts['B'] % 2) + 45 * (counts['B'] // 2)
    result += 20 * counts['C'] + 15 * counts['D']
    result += 15 * counts['D']
    result += 40 * counts['E']

    return result


