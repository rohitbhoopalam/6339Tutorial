import nltk
from nltk.collocations import *
import re

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

data = nltk.corpus.genesis.words('english-web.txt')
print len(data), "words data"

finder = BigramCollocationFinder.from_words(data)
finder.apply_word_filter(lambda x: False if re.match('\w', x) else True)
print finder.nbest(bigram_measures.raw_freq, 20)  


finder1 = TrigramCollocationFinder.from_words(data)
finder1.apply_word_filter(lambda x: False if re.match('\w', x) else True)
print finder1.nbest(trigram_measures.raw_freq, 20)  
