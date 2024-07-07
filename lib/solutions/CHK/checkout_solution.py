# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skusChars = sorted(list(skus))
    alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    counts = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G': 0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    prices = {'A':50, 'B':30, 'C':20, 'D':15, 'E':40, 'F':10, 'G': 20, 'H':10, 'I':35, 'J':60, 'K':70, 'L':90, 'M':15, 'N':40, 'O':10, 'P':50, 'Q':30, 'R':50, 'S':20, 'T':20, 'U':40, 'V':50, 'W':20, 'X':17, 'Y':20, 'Z':21}
    freeItems = {'E': [[2, 'B']], 'N': [[3, 'M']], 'R': [[3, 'Q']]}
    modRules = {'A': [[5, 200], [3, 130]], 'B': [[2, 45]], 'F': [[3, 20]], 'H': [[10, 80], [5, 45]], 'K': [[2, 120]], 'P': [[5, 200]], 'Q': [[3, 80]], 'U': [[4, 120]], 'V': [[3, 130], [2, 90]]}
    multiBuyOffers = [[['Z', 'Y', 'T', 'S', 'X'], [3, 45]]]
    
    for s in skusChars:
        if s in alpha:
            counts[s] += 1
        else:
            return -1

    result = 0
    for offer in multiBuyOffers:
        b = 0
        for s in offer[0]:
            b += counts[s]
        
        while b >= offer[1][0]:
            print(b, counts)
            remainingOfferItems = offer[1][0]
            for s in offer[0]:
                c = min(remainingOfferItems, counts[s])
                remainingOfferItems -= c
                counts[s] -= c
                if remainingOfferItems == 0:
                    result += offer[1][1]
                    b -= offer[1][0]
                    remainingOfferItems = offer[1][0]
                
                if remainingOfferItems == offer[1][0]:
                    result += offer[1][1] * (counts[s] // offer[1][0])
                    b -= (counts[s] // offer[1][0]) * offer[1][0]
                    counts[s] %= offer[1][0]
    
    for s, u in freeItems.items():
        for v in u:
            if counts[s] > 1:
                if counts[s] // v[0] >= counts[v[1]]:
                    counts[v[1]] = 0
                else:
                    counts[v[1]] -= counts[s] // v[0]

    for s, u in modRules.items():
        for v in u:
            if counts[s] // v[0] > 0:
                result += v[1] * (counts[s] // v[0])
                counts[s] %= v[0]

    for s in alpha:
        result += prices[s] * counts[s]
    
    return result

print(checkout("STXSTX"))