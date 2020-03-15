from nltk.corpus import wordnet as wn
from time import time


def expand_query_globally(query: str) -> str:
    # FIXME
    # start = time()
    tokens = query.split()
    new_query = set()
    new_query.update(tokens)
    for token in tokens:
        new_query.update(get_synonyms(token))
    # print('expand_query_globally: %s seconds' % (time() - start))
    return ' '.join(new_query)


def get_synonyms(word: str) -> set:
    synonyms = set()
    for i, syn in enumerate(wn.synsets(word)):
        if i < 3:
            tmp = [e for e in syn.lemma_names() if e.isalpha()]
            tmp = tmp[:3]
            synonyms.update(tmp)
    return synonyms


if __name__ == '__main__':
    q = 'oil platform explosion'

    print(expand_query_globally(q))
