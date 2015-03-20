import nltk
from nltk.corpus import PlaintextCorpusReader
root = '/Users/rohitbhoopalam/rohit/uta_courses/sem2/6339/6339Tutorial/wiki_sample_data'
new_corpus = PlaintextCorpusReader(root, '.*')
print new_corpus.words()
