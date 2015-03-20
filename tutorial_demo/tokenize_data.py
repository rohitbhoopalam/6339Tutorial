import nltk
from nltk.corpus import inaugural 
import matplotlib.pyplot as plt

data = inaugural.raw()

tokens = nltk.word_tokenize(data)

count_dict = {}
count_list = []
plot_list = []

for token in tokens:
    plot_list.append(len(token))
    try:
        count_dict[len(token)] += 1
    except KeyError:
        count_dict[len(token)] = 1

    
for i in range(max(count_dict.keys())):
    try:
        count_list.append(count_dict[i])
    except KeyError:
        count_list.append(0)

plt.hist(plot_list, normed=True)
print count_list
print count_dict.keys()
#print max(count_dict.keys())
#plt.show()
