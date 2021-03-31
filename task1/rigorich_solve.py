import re
import string


def TextFromFile():
    DELIMETER = '\\'
    TEXTFILE = 'text.txt'
    path = __file__.replace(__file__[__file__.rfind(DELIMETER):], DELIMETER) + TEXTFILE
    file = open(path, 'r') 
    text = file.read()
    file.close()
    return text


def FrequencyList(s: str) -> list:
    cnt = {}
    for i in re.sub('[^\w\s]', ' ', s.lower().replace('\n', ' ')).split(' '):
        if (len(i) > 0):
            cnt.setdefault(i, 0)
            cnt[i] += 1
    return sorted(cnt.items(), key = lambda item: item[1], reverse = True)


def WordsCounts(s: str) -> list:
    cnt = []
    for p in re.sub('[^\w\s.]', '', re.sub('[!?]', '.', s)).split('.'):
        words = 0
        for i in p.split(' '):
            if (len(i) > 0):
                words += 1
        if (words > 0):
            cnt += [words]
    return cnt

def Average(l: list):
    return sum(l) / len(l)

def Median(l: list):
    l = sorted(l)
    return (l[len(l) // 2] + l[(len(l) - 1) // 2]) / 2


def Ngramms(s: str, K: int) -> str:
    cnt = {}
    s = re.sub('[^a-z]', '', s.lower())
    for i in range(len(s) - K + 1):
        subs = s[i:i+K]
        cnt.setdefault(subs, 0)
        cnt[subs] += 1
    return sorted(cnt.items(), key = lambda item: item[1], reverse = True)


def solve(text: str = None):
    print('1) Text statistics\n')
    if text is None:
        text = TextFromFile()
    print(text)
    print()
    print("-----")
    print("Frequency list:")
    print(FrequencyList(text))
    print("-----")
    print("Average amount of words in sentence:", Average(WordsCounts(text)))
    print("Median amount of words in sentence:", Median(WordsCounts(text)))
    print("-----")
    K = 4
    N = 10
    dct = Ngramms(text, K)
    print(f"Top-{N} {K}-gramms:")
    print([dct[i] for i in range(min(N, len(dct)))])
    print("-----")

#solve()