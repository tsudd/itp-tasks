# first solution

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


def process_text(text):
    assert type(text) == str

    statements = text.lover().split('.')
    words_stat = {}
    statement_words_count = 0

    for statement in statements:
        words = statement.replace()



def solve(text=TEXT_EXAMPLE):
    print("Processing text:")
    print(text)


