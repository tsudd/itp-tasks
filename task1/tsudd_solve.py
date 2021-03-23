import re

TEXT_EXAMPLE = "By some measures, Joe Biden has gotten off to a slow start as President. His transition was stalled by " \
              "Donald Trump’s refusal to acknowledge defeat. His Cabinet nominees are taking longer than most to be " \
              "confirmed by the Senate. And he’s signing his first major piece of legislation, the COVID-relief" \
              " bill, " \
              "almost a month later in his term than Barack Obama enacted a major economic recovery " \
              "package 12 years ago." \
              "But Biden\'s first 50 days have, in fact, had far-reaching impact. The $1.9 trillion " \
              "American Rescue Plan, which Biden signed into law March 11, will affect tens of millions of " \
              "Americans directly, through cash payments, a massive boost in childcare aid, student loan support, " \
              "expanded healthcare and housing assistance. At the same time, " \
              "Biden\'s team of government veterans has executed a series of less " \
              "visible but consequential moves that affect the U.S. at home and abroad, " \
              "from increasing vaccine production and approving loans for multitudes of " \
              "struggling small businesses to rolling back counter-terrorism missions in America\'s shadow wars. " \
              "\"He is moving on two fronts, so something gets done every day,\" says Celinda Lake, " \
              "a Democratic pollster who was a senior adviser to the Biden campaign. \"[His] advantage " \
              "is the really in-depth understanding of the process,\" says Lake, and “his understanding of " \
              "the institutions. And that is true for all of his appointees as well.\" " \
              "Biden and Vice President Kamala Harris will travel the country beginning next week to sell the relief " \
              "plan, and his other 50-day accomplishments, and to try to build on " \
              "surprising popularity for his moves so far. A poll released March 5 by " \
              "the The Associated Press-NORC Center for Public Affairs Research found Biden " \
              "had a 60 percent job approval rating. (A Quinnipiac poll had Trump\'s at 41 percent around this time. " \
              "Gallup had Obama\'s at 62 percent.) They will need all the backing they can muster. " \
              "The American Rescue Plan squeaked through Congress along party lines, casting doubt on Biden\'s " \
              "campaign pledge to build bipartisanship, and highlighting potential weak spots in the Democratic " \
              "Party\'s coalition. At the same time, the Administration faces a looming surge of migrants at " \
              "the U.S.-Mexico border that critics say has been fueled by Biden\'s reversal of some of Trump\'s " \
              "controversial immigration policies. Biden\'s aides and allies say he can keep delivering on his " \
              "promises. “I think this bill will actually build Joe Biden\'s political capital by making it clear " \
              "he\'s able to hold the Democratic caucus together, and he\'s able to push through successfully " \
              "a bold piece of legislation,\" says Delaware Sen. Chris Coons, a Biden protégé who occupies the " \
              "President\'s former Senate seat. “He\'s continuing his outreach to Republicans."

SYNTAX_SYMBOLS_REGEX = '[^\w\s]'
SYNTAX_SYMBOLS_AND_DOT_REGEX = '[^\w\s.]'
END_SYMBOLS_REGEX = '[!?]'

FILE_OUTPUT = True
OUTPUT_FILE_NAME = "dist.txt"
OUTPUT_TOPIC = "Text processing\n"
TABLE_TOPIC = "Word ==> count\n"


def process_text(text, fp=None):
    assert type(text) == str

    words = re.sub(SYNTAX_SYMBOLS_REGEX, ' ', text.lower().replace('\n', ' ')).split(' ')
    words_stat = {}
    words_count = 0
    statement_words = []

    for word in words:
        if len(word) == 0:
            continue
        words_count += 1
        try:
            words_stat[word] += 1
        except KeyError:
            words_stat[word] = 1
    for sentence in re.sub(SYNTAX_SYMBOLS_AND_DOT_REGEX, ' ', re.sub(END_SYMBOLS_REGEX, '.', text)).split('.'):
        count = 0
        for word in sentence.split(' '):
            if len(word) > 0:
                count += 1
        if count > 0:
            statement_words.append(count)

    print_stats(words_stat, fp)
    average_words_amount(statement_words, fp)
    median_word_count(statement_words, fp)


def print_stats(words_stat, fp=None):
    assert type(words_stat) == dict

    sorted(words_stat.items(), key=lambda item: item[1], reverse=True)
    if fp:
        fp.write(TABLE_TOPIC)
        for k, v in words_stat.items():
            fp.write(f"{k:30} ==> {v:10d}\n")
    else:
        print(TABLE_TOPIC)
        for k, v in words_stat.items():
            print(f"{k:30} ==> {v:10d}\n")


def average_words_amount(words_amount: list,  fp=None):
    s = f"Average words amount in one sentence is {round(sum(words_amount) / len(words_amount), 1)}.\n"

    if fp:
        fp.write(s)
    else:
        print(s)


def median_word_count(words_count, fp=None):
    assert type(words_count) == list

    words_count.sort()
    num = (words_count[len(words_count) // 2] + words_count[(len(words_count) - 1) // 2]) / 2
    s = f"Median word amount in one sentence is {num}.\n"
    if fp:
        fp.write(s)
    else:
        print(s)


def solve(text=TEXT_EXAMPLE):
    if FILE_OUTPUT:
        fp = open(OUTPUT_FILE_NAME, "w")
        fp.write(OUTPUT_TOPIC)
        process_text(text, fp)
    else:
        print(OUTPUT_TOPIC)
        print(text)
        process_text(text)


