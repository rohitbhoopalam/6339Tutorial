import nltk
from nltk.tokenize import sent_tokenize

data = """Hands down this is my favorite in DFW so far. The pork spring rolls are perfection and the pho just dominates. I've taken a couple of years to try other places and nobody really compares in the area.

Apparently my old review was deleted when I updated it. Okay so here's the scoop then! """


sent = sent_tokenize(data)

print sent
print len(sent)
