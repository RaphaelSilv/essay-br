from build_dataset import Corpus
from stats import Statistic

c = Corpus()

prompts = c.read_prompt('prompts.csv')
corpus = c.read_corpus('extended_essay-br.csv')

print(prompts.shape)
print(corpus.shape)

# statistics = Statistic(corpus)
# print(statistics.statistics_essays())
