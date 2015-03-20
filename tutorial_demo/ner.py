import nltk

data = """Musk was born June 28, 1971, in Pretoria, Gauteng, South Africa,[17] to a Canadian-English mother and prominent model Maye Musk and a South African-born British father and electrical/mechanical engineer Errol Musk.[18][19][20] After his parents divorced in 1980, Musk lived mostly with his father in locations in South Africa.[21] He taught himself computer programming and at age 12 sold the computer code for a video game called Blastar for $500."""

tokens = nltk.word_tokenize(data)

tagged = nltk.pos_tag(tokens)

entities = nltk.chunk.ne_chunk(tagged)

print entities 
