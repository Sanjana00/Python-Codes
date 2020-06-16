from collections import Counter

def countwords():
    c = Counter()
    for line in open('warandpeace.txt'):
        c.update(line.split())
    return c.most_common(10)

for word, freq in countwords():
    print('{} {}'.format(word, freq))
