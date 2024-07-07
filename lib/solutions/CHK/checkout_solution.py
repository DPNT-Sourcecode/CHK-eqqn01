# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    skusChars = sorted(list(upper(skus)))
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for s in skusChars:
        counts[s] += 1
    return 50 * counts['A'] % 3 + 130 * counts['A'] // 3 + 30 * counts['B'] % 2 + 45 * counts['B'] // 2 + 20 * counts['C'] + 15 * counts['D']

