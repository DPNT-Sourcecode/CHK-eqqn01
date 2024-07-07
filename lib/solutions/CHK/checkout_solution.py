# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skusChars = sorted(list(skus))
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    counts = {(x, 0) for x in alpha}
    prices = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40, 'F':10, 'G': 20, 'H':10, 'I':35, 'J':60, 'K':80, 'L':90, 'M':15, 'N':40, 'O':10, 'P':50, 'Q':30, 'R':50, 'S':30, 'T':20, 'U':40, 'V':50, 'W':20, 'X':90, 'Y':10, 'Z':50}
    freeItems = {'E': [(2, 'B')], 'N': [(3, 'M')], 'R': [(3, 'Q')]}
    modRules = {'A': [(5, 200), (3, 130)], 'B': [(2, 45)], 'F': [(3, 20)], 'H': [(10, 80), (4, 45)], 'K': [(2, 150)], 'P': [(5, 200)], 'Q': [(3, 80)], 'U': [(4, 120)], 'V': [(3, 130), (2, 90)]}

    if len(skusChars) == 0:
        return -1
    
    for s in skusChars:
        if s in alpha:
            counts[s] += 1
        else:
            return -1

    result = 0

    for s, v in freeItems:
        if counts[s] > 1:
            if counts[s] // v[0] >= counts[v[1]]:
                counts[v[1]] = 0
            else:
                counts[v[0]] -= counts[s] // v[0]

    for s, v in modRules:
        if counts[s] // v[0] > 0:
            result = v[1] * (counts[s] // v[0])
            counts[s] %= v[0]

    for s in alpha:
        result += prices[s] * counts[s]
    
    return result



